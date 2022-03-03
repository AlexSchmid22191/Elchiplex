from PySide2.QtCore import QObject, Signal


class GuiSignals(QObject):
    request_ports = Signal()
    connect_device = Signal(str)
    disconnect_device = Signal()

    toggle_single_relay = Signal((tuple, bool))
    toggle_all_relays = Signal(dict)


class EngineSignals(QObject):
    single_relay_state = Signal((tuple, bool))
    all_relays_state = Signal(dict)


sig_engine = EngineSignals()
sif_gui = GuiSignals()
