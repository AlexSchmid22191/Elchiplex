from PySide2.QtCore import Qt
from PySide2.QtGui import QFontDatabase, QPixmap
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from src.ComSignals import EngineSignals, GuiSignals
from src.Interface.ElchDeviceMenu import ElchDeviceMenu
from src.Interface.ElchPresets import ElchPresets
from src.Interface.ElchRelayControl import ElchRelayControl
from src.Interface.ElchStatusBar import ElchStatusBar
from src.Interface.ElchTitleBar import ElchTitlebar


class ElchMainWindow(QWidget):
    def __init__(self, engine_signals: EngineSignals, gui_signals: GuiSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.engine_signals = engine_signals
        self.gui_signals = gui_signals

        self.setWindowFlags(Qt.FramelessWindowHint)

        QFontDatabase.addApplicationFont('Fonts/Roboto-Light.ttf')
        QFontDatabase.addApplicationFont('Fonts/Roboto-Regular.ttf')

        with open('Interface/style.qss') as stylefile:
            self.setStyleSheet(stylefile.read())

        self.device_menu = ElchDeviceMenu(engine_signals, gui_signals)
        self.titlebar = ElchTitlebar()
        self.statusbar = ElchStatusBar(engine_signals)
        self.relaycontrol = ElchRelayControl(engine_signals, gui_signals)
        self.presets = ElchPresets(engine_signals, gui_signals)

        elchicon = QLabel(objectName='Icon')
        elchicon.setPixmap(QPixmap('Interface/Icons/ElchiHead.png'))

        panel_spacing = 20

        hbox_inner = QHBoxLayout()
        hbox_inner.addWidget(self.relaycontrol, stretch=0)
        hbox_inner.addWidget(self.presets, stretch=0)

        vbox_inner = QVBoxLayout()
        vbox_inner.addLayout(hbox_inner)
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
