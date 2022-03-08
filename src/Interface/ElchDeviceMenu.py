from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton


class ElchDeviceMenu(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setAttribute(Qt.WA_StyledBackground, True)

        self.port_menu = QComboBox()
        self.connect_button = QPushButton(text='Connect', objectName='Connect')
        self.refresh_button = QPushButton(text='Refresh Serial', objectName='Refresh')

        self.connect_button.toggled.connect(self.connect_device)
        self.connect_button.setCheckable(True)

        vbox = QVBoxLayout()
        vbox.setSpacing(10)
        vbox.setContentsMargins(10, 10, 10, 10)

        vbox.addWidget(self.port_menu)
        vbox.addWidget(self.connect_button)
        vbox.addWidget(self.refresh_button)
        vbox.addStretch()
        self.setLayout(vbox)

    def update_ports(self, ports):
        self.port_menu.clear()
        self.port_menu.addItems(ports)
        for port, description in ports.items():
            index = self.port_menu.findText(port)
            self.port_menu.setItemData(index, description, Qt.ToolTipRole)

    def connect_device(self, state):
        port = self.port_menu.currentText()
        print(state)
