import functools

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, \
    QApplication

from src.ComSignals import EngineSignals, GuiSignals


class ElchPresets(QWidget):
    def __init__(self, engine_signals: EngineSignals, gui_signals: GuiSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.engine_signals = engine_signals
        self.gui_signals = gui_signals

        self.setAttribute(Qt.WA_StyledBackground, True)

        self.preset_buttons = {i: QPushButton(f'Preset {i}') for i in range(1, 5)}

        button_box = QVBoxLayout()
        button_box.addStretch()
        button_box.addWidget(QLabel('Presets', objectName='Header'))
        for idx, button in self.preset_buttons.items():
            button_box.addWidget(button)
            button.setToolTip('Click to apply preset. Shift+Click to\nset current configuration as preset.')
            button.clicked.connect(functools.partial(self.preset_button_click, idx))
        button_box.addStretch()

        self.setLayout(button_box)

    def preset_button_click(self, button):
        modifiers = QApplication.keyboardModifiers()
        match modifiers:
            case Qt.ShiftModifier:
                self.gui_signals.save_preset.emit(button)
            case _:
                self.gui_signals.load_preset.emit(button)
