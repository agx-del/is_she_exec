# coding=utf-8
import sys
import csv
import numpy as np
import cv2


class Data():
    def __init__(self):
        pass

    def get_unit(self):
        pass


class Dataset():
    def __init__(self, fn=None):
        self.X = np.array([])
        self.Y = np.array([])

    def get_data(self):
        pass


class TrainData(Data):
    def __init__(self, fn):
        super(TrainData, self).__init__()
        self.fn = fn

    def get_unit(self):
        super(TrainData, self).get_unit()
        return cv2.imread(self.fn)


class TrainDataset(Dataset):
    def __init__(self, fn=None):
        super(TrainDataset, self).__init__()
        self.fns = np.array([])
        self.fn = fn
        self.pic_base_dir = "./pic/"
        if fn is not None:
            self.reader = csv.reader(open(self.fn, "r"))

    def setPicBaseDir(self, dir):
        self.pic_base_dir = dir

    def get_data(self):
        super(TrainDataset, self).get_data()
        for item in self.reader:
            t_data = TrainData(self.pic_base_dir+item[0])
            #print("read uri:%s" % str(self.pic_base_dir+item[0]))
            self.fns = np.append(self.fns, item[0])
            self.Y = np.append(self.Y, item[1]*1)
            img = t_data.get_unit()
            if self.reader.line_num == 1:
                self.X = img[np.newaxis, :, :, :]
            else:
                self.X = np.concatenate(
                    [self.X, img[np.newaxis, :, :, :]], axis=0)


if __name__ == "__main__":
    ds = TrainDataset("../data/train.csv")
    ds.setPicBaseDir("../pic/")
    ds.get_data()
    print("X shape is :%s" % str(ds.X.shape))
    print("Y shape is :%s" % str(ds.Y.shape))
    print(str(ds.Y))
    print(str(ds.fns))

    for item in ds.X:
        print(str(item[0:10, 100, 1]))
        print("************************************")
