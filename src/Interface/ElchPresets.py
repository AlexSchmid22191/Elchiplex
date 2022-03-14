import functools

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, \
    QApplication


class ElchPresets(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        print(button)
        match modifiers:
            case Qt.ShiftModifier:
                print('shift')
            case Qt.ControlModifier:
                print('ctrl')
            case _:
                print('click')
