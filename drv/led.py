import RPi.GPIO as GPIO
import time


class Drv():
    def __init__(self):
        pass


class Led(Drv):
    def __init__(self):
        super(Led, self).__init__()
        self.GREEN_PIN = 35
        self.BLUE_PIN = 33
        self.RED_PIN = 37
        GPIO.setmode(GPIO.BOARD)
        self.setAllOff()

    def __setLedOn(self, pin):
        self.setAllOff()
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    def __setLedOff(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup(pin)

    def setGreenOn(self):
        self.__setLedOn(self.GREEN_PIN)

    def setGreenOff(self):
        self.__setLedOff(self.GREEN_PIN)

    def setRedOn(self):
        self.__setLedOn(self.RED_PIN)

    def setRedOff(self):
        self.__setLedOff(self.RED_PIN)

    def setBlueOn(self):
        self.__setLedOn(self.BLUE_PIN)

    def setBlueOff(self):
        self.__setLedOff(self.BLUE_PIN)

    def setGreenOnTime(self, second):
        self.setGreenOn()
        time.sleep(second)
        self.setGreenOff()

    def setRedOnTime(self, second):
        self.setRedOn()
        time.sleep(second)
        self.setRedOff()

    def setBlueOnTime(self, second):
        self.setBlueOn()
        time.sleep(second)
        self.setBlueOff()

    def setGreenRedOnTime(self, state, second):
        if state == 1:
            self.setGreenOnTime(second)

        elif state == 0:
            self.setRedOnTime(second)
        else:
            assert "ERROR: Led.setGreenState() - error state!"

    def setAllOff(self):
        self.__setLedOff(self.GREEN_PIN)
        self.__setLedOff(self.RED_PIN)
        self.__setLedOff(self.BLUE_PIN)


if __name__ == "__main__":
    led = Led()
    led.setGreenOnTime(1)
