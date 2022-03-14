from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from PySide2.QtWinExtras import QtWin

from Interface.ElchMainWindow import ElchMainWindow
from Engine.Engine import ElchiplexEngine
from ComSignals import GuiSignals, EngineSignals

def main():
    QtWin.setCurrentProcessExplicitAppUserModelID('elchworks.elchiplex.1.0')
    app = QApplication()
    app.setWindowIcon(QIcon('Interface/Icons/Logo.ico'))
    engine_signals = EngineSignals()
    gui_signals = GuiSignals()

    gui = ElchMainWindow(engine_signals, gui_signals)
    engine = ElchiplexEngine(engine_signals, gui_signals)
    app.exec_()


if __name__ == '__main__':
    main()
