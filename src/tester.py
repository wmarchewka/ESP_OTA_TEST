import time
from machine import Pin


class Tester(object):
    def __init__(self):
        self.led=Pin(15,Pin.OUT)
        self.run()

    def run(self):
        while True:
            led.value(1)
            time.sleep(0.5)
            led.value(0)
            time.sleep(0.5)


