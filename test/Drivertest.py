import src.Driver.Omniplex
import time

device = src.Driver.Omniplex.Omniplex('COM11')
time.sleep(3)

print(device.read_all_relays())
device.set_single_relay((1, 1), True)
print(device.read_all_relays())
time.sleep(1)
device.set_all_relays({(left, right): right % 2 for left in range(1, 5) for right in range(1, 5)})
print(device.read_all_relays())

while True:
    pass
