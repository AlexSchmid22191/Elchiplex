import os
import time
import json
import serial.tools.list_ports
from PySide2.QtCore import Slot
from src.Driver.Omniplex import Omniplex


class ElchiplexEngine:
    def __init__(self):
        self.available_ports = {port[0]: port[1] for port in serial.tools.list_ports.comports()}
        self.device = None

        if os.path.exists('presets.json'):
            try:
                self._load_presets()
            except InvalidPreset:
                self.presets = self._create_empty_presets()
        else:
            self.presets = self._create_empty_presets()

    def connect_device(self, port):
        self.device = Omniplex(port)
        time.sleep(2)

    def refresh_available_ports(self):
        self.available_ports = {port[0]: port[1] for port in serial.tools.list_ports.comports()}

    def set_single_relay(self, relay: tuple, state: bool) -> None:
        # Here goes the Qthread implementation
        pass

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
        return {preset_idx: {(i, j): False for i in range(1, 5 ) for j in range(1, 5)} for preset_idx in range(1, 5)}


class InvalidPreset(Exception):
    """Is raised when a preset configuration does not contain the entries for all relais in each of 4 presets"""
    pass
