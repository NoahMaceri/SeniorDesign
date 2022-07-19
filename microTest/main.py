import machine
import time

redLED = machine.Pin(2, machine.Pin.OUT)

if __name__ == '__main__':
    for x in range(5):
        time.sleep(0.5)
        redLED.on()
        time.sleep(0.5)
        redLED.off()

