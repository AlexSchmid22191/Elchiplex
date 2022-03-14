from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton

from src.ComSignals import EngineSignals, GuiSignals


class ElchDeviceMenu(QWidget):
    def __init__(self, engine_signales: EngineSignals, gui_signals: GuiSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.engine_signals = engine_signales
        self.gui_signals = gui_signals

        self.setAttribute(Qt.WA_StyledBackground, True)

        self.port_menu = QComboBox()
        self.connect_button = QPushButton(text='Connect', objectName='Connect')
        self.refresh_button = QPushButton(text='Refresh Serial', objectName='Refresh')

        self.connect_button.toggled.connect(self.connect_device)
        self.refresh_button.clicked.connect(self.gui_signals.request_ports.emit)
        self.connect_button.setCheckable(True)

        vbox = QVBoxLayout()
        vbox.setSpacing(10)
        vbox.setContentsMargins(10, 10, 10, 10)

        vbox.addWidget(self.port_menu)
        vbox.addWidget(self.connect_button)
        vbox.addWidget(self.refresh_button)
        vbox.addStretch()
        self.setLayout(vbox)

        self.engine_signals.available_ports.connect(self.update_ports)

    def update_ports(self, ports):
        self.port_menu.clear()
        self.port_menu.addItems(ports)
        for port, description in ports.items():
            index = self.port_menu.findText(port)
            self.port_menu.setItemData(index, description, Qt.ToolTipRole)

    def connect_device(self, state):
        port = self.port_menu.currentText()
        if state:
            self.gui_signals.connect_device.emit(port)
        else:
            self.gui_signals.disconnect_device.emit()
