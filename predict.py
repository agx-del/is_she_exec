# coding=utf-8
import numpy as np
import model.model
import drv.led
import datetime


play_model = model.model.PlayModel(filename="temp.h5")
led = drv.led.Led()

for i in range(10):
    start = datetime.datetime.now()
    predict = play_model.pred_pic()
    end = datetime.datetime.now()
    led.setGreenRedOnTime(predict, 1)

    print("pridict is:%s" % str(predict))
    print("run time is:%s" % str(end - start))
