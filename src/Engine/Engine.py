import functools
import json
import time

import serial.tools.list_ports

from src.ComSignals import EngineSignals, GuiSignals
from src.Driver.Omniplex import Omniplex
from src.Engine.QThread import Worker
from PySide2.QtCore import QThreadPool


class ElchiplexEngine:
    def __init__(self, engine_signales: EngineSignals, gui_signals: GuiSignals):
        self.engine_signals = engine_signales
        self.gui_signals = gui_signals

        self.available_ports = {port[0]: port[1] for port in serial.tools.list_ports.comports()}
        self.engine_signals.available_ports.emit(self.available_ports)
        self.device = None

        try:
            self._load_presets()
        except (InvalidPreset, FileNotFoundError):
            self.presets = self._create_empty_presets()
            self._save_presets()

        self.gui_signals.connect_device.connect(self.connect_device)
        self.gui_signals.disconnect_device.connect(self.disconnect_device)
        self.gui_signals.request_ports.connect(self.refresh_available_ports)

        self.pool = QThreadPool()

    def connect_device(self, port):
        self.device = Omniplex(port)
        time.sleep(2)
        self.engine_signals.device_connected.emit(port)

        self.gui_signals.toggle_single_relay.connect(self.set_single_relay)

    def disconnect_device(self):
        self.device.serial.close()
        self.device = None
        self.engine_signals.device_disconnectd.emit()

        self.gui_signals.toggle_single_relay.disconnect(self.set_single_relay)

    def refresh_available_ports(self):
        self.available_ports = {port[0]: port[1] for port in serial.tools.list_ports.comports()}
        self.engine_signals.available_ports.emit(self.available_ports)

    def set_single_relay(self, relay: tuple, state: bool) -> None:
        worker = Worker(functools.partial(self.device.set_single_relay, relay, state))
        self.pool.start(worker)

    def _load_presets(self):
        with open('presets.json', 'r') as file:
            data = json.loads(file.read())
        data = {json.loads(preset_idx): {tuple(json.loads(relay)): state for relay, state in preset.items()}
                for preset_idx, preset in data.items()}
        if not self._validate_preset(data):
            raise InvalidPreset('Invalid preset file!')
        self.presets = data

    def _save_presets(self):
        data = {preset_idx: {json.dumps(relay): state for relay, state in preset.items()}
                for preset_idx, preset in self.presets.items()}
        with open('presets.json', 'w') as file:
            file.write(json.dumps(data))

    @staticmethod
    def _validate_preset(presets: dict) -> bool:
        preset_keys = {1, 2, 3, 4}
        relay_keys = {(i, j) for j in range(1, 5) for i in range(1, 5)}

        return set(presets.keys()) == preset_keys and \
               all([set(inner_keys) == relay_keys for inner_keys in presets.values()])

    @staticmethod
    def _create_empty_presets() -> dict:
        return {preset_idx: {(i, j): False for i in range(1, 5) for j in range(1, 5)} for preset_idx in range(1, 5)}


class InvalidPreset(Exception):
    """Is raised when a preset configuration does not contain the entries for all relais in each of 4 presets"""
    pass
