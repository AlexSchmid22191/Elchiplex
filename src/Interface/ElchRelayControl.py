from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QGridLayout, QPushButton, \
    QGraphicsScene, QGraphicsView, QApplication
import functools


class ElchRelayControl(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

    @staticmethod
    def checkbox_toogled(state: bool, relay: tuple):
        print(state, relay)

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
