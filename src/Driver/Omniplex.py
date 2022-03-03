import time
import minimalmodbus
from PySide2.QtCore import QMutex


class Omniplex(minimalmodbus.Instrument):
    def __init__(self, portname: str, slaveadress: int = 1, baudrate: int = 9600) -> None:
        super().__init__(portname, slaveadress)
        self.serial.baudrate = baudrate
        self.com_mutex = QMutex()
        time.sleep(2)

    def set_single_relay(self, relay: tuple, state: bool) -> None:
        self.write_bit(self._relay_to_address(relay), state, functioncode=5)

    def read_single_relay(self, relay: tuple) -> bool:
        return bool(self.read_bit(self._relay_to_address(relay), functioncode=1))

    def set_all_relays(self, states: dict) -> None:
        states = [states[relay] for relay in map(self._address_to_relay, range(16))]
        self.write_bits(0, states)

    def read_all_relays(self) -> dict:
        states = self.read_bits(0, 16, functioncode=1)
        return {self._address_to_relay(address): states[address] for address in range(16)}

    @staticmethod
    def _address_to_relay(adress: int) -> tuple:
        return adress // 4 + 1, adress % 4 + 1

    @staticmethod
    def _relay_to_address(relay: tuple) -> int:
        return (relay[0] - 1) * 4 + relay[1] - 1
