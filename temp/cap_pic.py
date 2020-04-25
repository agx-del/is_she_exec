import picamera
from time import sleep
import drv.led


def main():

    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    for i in range(200, 300):
        camera.capture('./pic/image%s.jpg' % i)
        print('saved ./pic/image%s.jpg' % i)
        sleep(15)


if __name__ == "__main__":
    main()
