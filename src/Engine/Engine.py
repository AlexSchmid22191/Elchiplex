import time
import serial.tools.list_ports
from PySide2.QtCore import Slot
from src.Driver.Omniplex import Omniplex


class ElchiplexEngine:
    def __init__(self):
        self.available_ports = {port[0]: port[1] for port in serial.tools.list_ports.comports()}
        self.device = None

    @Slot(str)
    def connect_device(self, port):
        self.device = Omniplex(port)
        time.sleep(2)

    def refresh_available_ports(self):
        self.available_ports = {port[0]: port[1] for port in serial.tools.list_ports.comports()}

    def set_single_relay(self, relay: tuple, state: bool) -> None:
        # Here goes the Qthread implementation
        pass
