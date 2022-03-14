import functools

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QGridLayout, QApplication

from src.ComSignals import EngineSignals, GuiSignals


class ElchRelayControl(QWidget):
    def __init__(self, engine_signals: EngineSignals, gui_signals: GuiSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.engine_signals = engine_signals
        self.gui_signals = gui_signals

        self.setAttribute(Qt.WA_StyledBackground, True)

        self.toggle_buttons = {(row, col): QCheckBox() for row in range(1, 5) for col in range(1, 5)}

        grid = QGridLayout()
        for idx in range(1, 5):
            grid.addWidget(QLabel(str(idx)), 1, idx + 1)
            grid.addWidget(QLabel(str(idx)), idx + 1, 1)
        for (row, col), button in self.toggle_buttons.items():
            grid.addWidget(button, row + 1, col + 1)
            button.toggled.connect(functools.partial(self.checkbox_toogled, relay=(row, col)))
        grid.addWidget(QLabel('A', objectName='Header', alignment=Qt.AlignCenter), 0, 2, 1, 4)
        grid.addWidget(QLabel('B', objectName='Header', alignment=Qt.AlignCenter), 2, 0, 4, 1)

        grid_box = QVBoxLayout()
        grid_box.addLayout(grid)
        grid_box.addStretch()

        self.setLayout(grid_box)

    def checkbox_toogled(self, state: bool, relay: tuple):
        self.gui_signals.toggle_single_relay.emit(relay, state)


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
