import functools

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QGridLayout, QApplication

from src.ComSignals import EngineSignals, GuiSignals


class ElchRelayControl(QWidget):
    def __init__(self, engine_signals: EngineSignals, gui_signals: GuiSignals, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.engine_signals = engine_signals
        self.gui_signals = gui_signals

        self.engine_signals.all_relays_state.connect(self.update_checkboxes)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.checkboxes = {(row, col): QCheckBox() for row in range(1, 5) for col in range(1, 5)}

        grid = QGridLayout()
        for idx in range(1, 5):
            grid.addWidget(QLabel('R' + str(idx)), 1, idx + 1)
            grid.addWidget(QLabel('L' + str(idx)), idx + 1, 1)
        for (row, col), checkbox in self.checkboxes.items():
            grid.addWidget(checkbox, row + 1, col + 1)
            checkbox.toggled.connect(functools.partial(self.checkbox_toogled, relay=(row, col)))

        grid_box = QVBoxLayout()
        grid_box.addWidget(QLabel('Relays', objectName='Header', alignment=Qt.AlignCenter))
        grid_box.addLayout(grid)
        grid_box.addStretch()

        self.setLayout(grid_box)

    def checkbox_toogled(self, state: bool, relay: tuple):
        self.gui_signals.toggle_single_relay.emit(relay, state)

    def update_checkboxes(self, states: dict) -> None:
        """Update the state of the checckboxes with data from the engine"""
        for (row, col), checkbox in self.checkboxes.items():
            checkbox.blockSignals(True)
            checkbox.setChecked(states[(row, col)])
            checkbox.blockSignals(False)

