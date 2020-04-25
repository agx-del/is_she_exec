# coding=utf-8
import numpy as np
import model.model
import datasets.datasets
import cv2


train_data = datasets.datasets.TrainDataset("./data/train.csv")
train_data.get_data()
test_data = datasets.datasets.TrainDataset("./data/test.csv")
test_data.get_data()

print("X shape:%s" % str(train_data.X.shape))
print("Y shape:%s" % str(train_data.Y.shape))
#print("Y is:%s" % str(train_data.Y))

play_model = model.model.PlayModel(train_data.X[0].shape)
play_model.loss_train(train_data.X, train_data.Y,
                      test_data.X, test_data.Y, 8, 150)
predict = play_model.pred_pic("./pic/image275.jpg")
print("pridict is:%s" % str(predict))
# play_model.save("temp.h5")
