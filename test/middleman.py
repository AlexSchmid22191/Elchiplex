from PySide2.QtCore import QObject, Signal


class Communicate(QObject):
    test_sig = Signal((str, str))


com = Communicate()
