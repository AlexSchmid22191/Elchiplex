from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel


class ElchStatusBar(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.label = QLabel('Status')

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addStretch()

        self.setLayout(hbox)
