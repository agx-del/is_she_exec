import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)


def LedOn(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


def LedOff(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def LedFlash(pin):
    LedOn(pin)
    time.sleep(0.1)
    LedOff(pin)


def main():
    LedOff(33)
    LedOff(35)
    LedOff(37)
    while True:
        LedFlash(33)
        LedFlash(33)
        LedFlash(33)
        LedFlash(37)
        LedFlash(37)
        LedFlash(37)


if __name__ == "__main__":
    main()
