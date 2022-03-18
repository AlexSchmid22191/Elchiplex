from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel
from src.ComSignals import EngineSignals


class ElchStatusBar(QWidget):
    def __init__(self, engine_signals: EngineSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.engine_signals = engine_signals
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.label = QLabel('')

        self.timer = QTimer()

        self.engine_signals.single_relay_state.connect(self.display_relay_activity)
        self.engine_signals.device_connected.connect(self.display_device_connected)
        self.engine_signals.device_disconnectd.connect(self.display_device_disconnected)
        self.engine_signals.preset_loaded.connect(self.display_preset_load)
        self.engine_signals.preset_saved.connect(self.display_preset_save)

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addStretch()

        self.setLayout(hbox)

    def display_relay_activity(self, relay: tuple, state: bool) -> None:
        self.label.setText(f'Relay {relay} switched {"on" if state else "off"}!')
        self.timer.singleShot(2000, self.clear_label)

    def display_device_connected(self, port: str) -> None:
        self.label.setText(f'Device connected at {port}!')
        self.timer.singleShot(2000, self.clear_label)

    def display_device_disconnected(self) -> None:
        self.label.setText(f'Device disconnected!')
        self.timer.singleShot(2000, self.clear_label)

    def display_preset_load(self, preset_id: int) -> None:
        self.label.setText(f'Preset {preset_id} loaded!')
        self.timer.singleShot(2000, self.clear_label)

    def display_preset_save(self, preset_id: int) -> None:
        self.label.setText(f'Preset {preset_id} saved!')
        self.timer.singleShot(2000, self.clear_label)

    def clear_label(self):
        self.label.setText('')
