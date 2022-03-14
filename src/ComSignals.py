from PySide2.QtCore import QObject, Signal


class GuiSignals(QObject):
    request_ports = Signal()
    connect_device = Signal(str)
    disconnect_device = Signal()

    toggle_single_relay = Signal((tuple, bool))
    toggle_all_relays = Signal(dict)

    load_preset = Signal(int)
    save_preset = Signal(int)


class EngineSignals(QObject):
    available_ports = Signal(dict)

    single_relay_state = Signal((tuple, bool))
    all_relays_state = Signal(dict)

    device_connected = Signal(str)
    device_disconnectd = Signal()

