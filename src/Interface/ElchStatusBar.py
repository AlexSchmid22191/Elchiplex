from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel
from src.ComSignals import EngineSignals


class ElchStatusBar(QWidget):
    def __init__(self, engine_signals: EngineSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.engine_signals = engine_signals
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.label = QLabel('')

        self.engine_signals.single_relay_state.connect(self.display_relay_activity)
        self.engine_signals.device_connected.connect(self.display_device_connected)
        self.engine_signals.device_disconnectd.connect(self.display_device_disconnected)

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addStretch()

        self.setLayout(hbox)

    def display_relay_activity(self, relay: tuple, state: bool) -> None:
        self.label.setText(f'Relay {relay} switched {"on" if state else "off"}!')

    def display_device_connected(self, port: str) -> None:
        self.label.setText(f'Device connected at {port}!')

    def display_device_disconnected(self) -> None:
        self.label.setText(f'Device disconnected!')
