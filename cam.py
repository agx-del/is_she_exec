from time import sleep
import picamera
import drv.led
import model.model
import datetime
import count


def main():
    cnt = 1000
    play_model = model.model.PlayModel(filename="night_good.h5")
    led = drv.led.Led()
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    stCnt = count.Count()
    for i in range(0, cnt):
        # led.setBlueOnTime(0.5)
        pic_fn = './pic/temp.jpg'
        camera.capture(pic_fn)
        start = datetime.datetime.now()
        predict = play_model.pred_pic(pic_fn)
        end = datetime.datetime.now()
        if predict > 0.5:
            stCnt.setState(True)
        else:
            stCnt.setState(False)
        if stCnt.getLastState() == True:
            led.setGreenOn()
        else:
            led.setRedOn()
        print("pridict is: 【%s】" % str(predict), end=", ")
        print("during is:%s" % str(end - start))
        print("Play second during sum is: %d(s)" % stCnt.getStateDuring(True))
        sleep(1)

    led.setAllOff()


if __name__ == "__main__":
    main()
