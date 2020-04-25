# codeing: utf-8

import numpy as np
from keras import layers
from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
from keras.layers import AveragePooling2D, MaxPooling2D, Dropout, GlobalMaxPooling2D, GlobalAveragePooling2D
from keras.models import Model
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input
from keras.utils import to_categorical
from keras.models import load_model

import pydot
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
import numpy as np
from collections import deque

import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import datasets.datasets


class BaseModel():
    def __init__(self, input_shape=None, filename=None):
        if input_shape != None:
            self.input_shape = input_shape
            self.model = None
            self.create_model()
        if filename != None:
            self.load(filename)
        self.model.summary()

    def create_model(self):
        # Define the input placeholder as a tensor with shape input_shape. Think of this as your input image!
        X_input = Input(self.input_shape)

        # Zero-Padding: pads the border of X_input with zeroes
        #X = ZeroPadding2D((3, 3))(X_input)

        # CONV -> BN -> RELU Block applied to X
        X = Conv2D(16, (3, 3), strides=(1, 1),
                   activation='relu', name='conv0')(X_input)
        X = BatchNormalization(axis=3, name='bn0')(X)
        X = Dropout(0.5)(X)

        # MAXPOOL
        X = MaxPooling2D((2, 2), name='max_pool')(X)

        # CONV -> BN -> RELU Block applied to X
        X = Conv2D(32, (5, 5), strides=(3, 3),
                   activation='relu',  name='conv1')(X)
        X = BatchNormalization(axis=3, name='bn1')(X)
        X = Dropout(0.5)(X)

        # CONV -> BN -> RELU Block applied to X
        X = Conv2D(64, (7, 7), strides=(5, 5),
                   activation='relu', name='conv2')(X)
        X = BatchNormalization(axis=3, name='bn2')(X)
        #X = Activation('relu')(X)
        X = Dropout(0.4)(X)

        # CONV
        X = Conv2D(4, (5, 5), strides=(1, 1),
                   activation='relu', name='conv3')(X)
        X = BatchNormalization(axis=3, name='bn3')(X)
        X = Dropout(0.4)(X)

        # FLATTEN X (means convert it to a vector) + FULLYCONNECTED
        X = Flatten()(X)
        X = Dense(10, activation='relu', name='fc1')(X)
        X = Dropout(0.5)(X)
        X = Dense(1, activation='sigmoid', name='fc2')(X)

        # Create model. This creates your Keras model instance, you'll use this instance to train/test the model.
        self.model = Model(inputs=X_input, outputs=X, name='BaseModel')

    def loss_train(self, X, Y, batch_size, epochs=1):
        in_Y = Y  # to_categorical(Y, num_classes=2)
        self.model.compile(
            optimizer="Adam", loss="binary_crossentropy", metrics=["accuracy"])
        self.model.fit(x=X, y=in_Y, batch_size=batch_size,
                       epochs=epochs, shuffle=True)

    def pred(self, in_x):
        return self.model.predict(np.expand_dims(in_x, axis=0))

    def save(self, filename):
        self.model.save(filename)

    def load(self, filename):
        self.model = load_model(filename)


class PlayModel(BaseModel):
    def __init__(self, input_shape=None, filename=None):
        super(PlayModel, self).__init__(input_shape, filename)

    def loss_train(self, train_X, train_Y, test_X, test_Y, batch_size, epochs=1):
        #super(PlayModel, self).loss_train(X, Y, batch_size, epochs=epochs)
        max_acc = 0
        for i in range(epochs):
            print("train round %d/%d" % (i+1, epochs))
            super(PlayModel, self).loss_train(
                train_X, train_Y, batch_size, epochs=1)
            scores = self.model.evaluate(test_X, test_Y)  # , verbose=0)
            print("current acc is : %s" % str(scores[1]))
            if scores[1] > max_acc:
                max_acc = scores[1]
                self.save("max.h5")
                print("max acc found! acc is : %s" % str(max_acc))
            else:
                print("less than max, max acc is : %s" % str(max_acc))
                self.save("temp.h5")

    def pred_data(self, in_x):
        predict_result = super(PlayModel, self).pred(in_x)
        # return np.argmax(predict_result)
        return predict_result[0][0]

    def pred_pic(self, pic_fn="./temp.jpg"):
        pic_data = datasets.datasets.TrainData(pic_fn)
        pic = pic_data.get_unit()
        print("predicting pic:%s" % pic_fn, end=", ")
        return self.pred_data(pic)
