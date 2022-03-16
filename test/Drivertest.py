import src.Driver.Omniplex
import time
import random

device = src.Driver.Omniplex.Omniplex('COM11')
time.sleep(2)


while True:
    device.set_single_relay((3, 2), True)
    time.sleep(1)
    device.set_single_relay((3, 2), False)
    time.sleep(1)