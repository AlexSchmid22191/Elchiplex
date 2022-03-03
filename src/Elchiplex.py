from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from PySide2.QtWinExtras import QtWin

from Interface.ElchMainWindow import ElchMainWindow
from Engine.Engine import ElchiplexEngine


def main():
    QtWin.setCurrentProcessExplicitAppUserModelID('elchworks.elchiplex.1.0')
    app = QApplication()
    app.setWindowIcon(QIcon('Interface/Icons/Logo.ico'))
    engine = ElchiplexEngine()
    gui = ElchMainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
