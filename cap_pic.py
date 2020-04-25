from time import sleep
import picamera
import drv.led
import model.model
import datetime


def main():
    start_id = 976
    play_model = model.model.PlayModel(filename="night_good.h5")
    led = drv.led.Led()
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    for i in range(start_id, start_id+200):
        # led.setBlueOnTime(0.5)
        pic_fn = './pic/image%s.jpg' % i
        camera.capture(pic_fn)
        print('saved %s' % pic_fn)

        start = datetime.datetime.now()
        predict = play_model.pred_pic(pic_fn)
        end = datetime.datetime.now()
        if predict > 0.3:
            led.setGreenOn()
        else:
            led.setRedOn()
        print("pridict is: 【%s】" % str(predict))
        #print("run time is:%s" % str(end - start))
        sleep(2)
    led.setAllOff()


if __name__ == "__main__":
    main()
