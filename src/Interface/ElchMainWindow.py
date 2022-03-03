import os

from PySide2.QtCore import Qt
from PySide2.QtGui import QFontDatabase, QPixmap
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSizeGrip, QLabel

from src.Interface.ElchDeviceMenu import ElchDeviceMenu
from src.Interface.ElchTitleBar import ElchTitlebar
from src.Interface.ElchStatusBar import ElchStatusBar
from src.Interface.ElchRelayControl import ElchRelayControl


class ElchMainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowFlags(Qt.FramelessWindowHint)

        QFontDatabase.addApplicationFont('Fonts/Roboto-Light.ttf')
        QFontDatabase.addApplicationFont('Fonts/Roboto-Regular.ttf')

        with open('Interface/style.qss') as stylefile:
            self.setStyleSheet(stylefile.read())

        self.device_menu = ElchDeviceMenu()
        self.titlebar = ElchTitlebar()
        self.statusbar = ElchStatusBar()
        self.relaycontrol = ElchRelayControl()

        elchicon = QLabel(objectName='Icon')
        elchicon.setPixmap(QPixmap('Interface/Icons/ElchiHead.png'))

        panel_spacing = 20

        vbox_inner = QVBoxLayout()
        vbox_inner.addWidget(self.relaycontrol, stretch=1)
        vbox_inner.addWidget(self.statusbar, stretch=0)
        vbox_inner.setSpacing(panel_spacing)
        vbox_inner.setContentsMargins(panel_spacing, panel_spacing, panel_spacing, panel_spacing)

        vbox_outer = QVBoxLayout()
        vbox_outer.addWidget(self.titlebar, stretch=0)
        vbox_outer.addLayout(vbox_inner, stretch=1)
        vbox_outer.setContentsMargins(0, 0, 0, 0)
        vbox_outer.setSpacing(0)

        vbox_left = QVBoxLayout()
        vbox_left.addWidget(elchicon, alignment=Qt.AlignHCenter)
        vbox_left.addWidget(self.device_menu)

        hbox_outer = QHBoxLayout()
        hbox_outer.addLayout(vbox_left, stretch=0)
        hbox_outer.addLayout(vbox_outer, stretch=1)
        hbox_outer.setContentsMargins(0, 0, 0, 0)
        hbox_outer.setSpacing(0)

        self.setLayout(hbox_outer)
        self.show()
