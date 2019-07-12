from __future__ import print_function

import sys
import xlwt
from xlwt import Workbook
import pandas as pd
from xlutils.copy import copy
import csv



print('Python: {}'.format(sys.version))

import pyabf
import numpy as np
import matplotlib.pyplot as plt

filename = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19122007.abf'

abf = pyabf.ABF(filename)
print(abf)

abf.setSweep(0)
print("sweep data (ADC):", abf.sweepY)
print("sweep command (DAC):", abf.sweepC)
print("sweep times (seconds):", abf.sweepX)


eventLengths = []
def dataPoints(begin, end):
    #global counter
    with open("19122007_events.csv", mode='a') as csvNew:
        writer = csv.writer(csvNew, delimiter=',')
        eventStats = []
        limit = 0
        counter = 0
        for n in range(begin, end):
            if (limit < 4):
                Y = str(float(abf.sweepY[n]))
                eventStats.append(Y)
                counter += 1
                limit += 1
        eventLengths.append(counter)
        writer.writerow(eventStats)
        csvNew.close()


# def merge():
#     ##run through every existing txt file in this directory
#     for n in range(0, counter+1):
#         #loadCSV = pd.read_csv(home + str(n)+".csv")
#         # direct = "C:\Users\Elijah\PycharmProjects\abfFiles\1-1 nome and 1 me\" + home + str(counter) + ".csv
#
#         loadCSV = pd.read_csv(r"C:\Users\Elijah\PycharmProjects\abfFiles\1-1 nome and 1 me\19122007_0.csv")
#         loadCSV2 = pd.read_csv(r"C:\Users\Elijah\PycharmProjects\abfFiles\1-1 nome and 1 me\19122007_1.csv")
#         # print(loadCSV)
#         array = [np.array(loadCSV), "nome"]
#         array2 = [np.array(loadCSV2), "1me"]
#         toMerge = (array, array2)
#         merged = np.concatenate(toMerge)
#         pd.DataFrame(merged).to_csv("merged.csv", header=None, index=None)



dataPoints(7396, 7400)
dataPoints(7950, 7964)
dataPoints(8044, 8067)
dataPoints(8067, 8201)
dataPoints(8263, 13924)
dataPoints(14242, 14255)
dataPoints(14402, 14441)
dataPoints(14515, 14519)
dataPoints(43399, 43405)
dataPoints(43489, 46505)
dataPoints(46532, 52376)
dataPoints(88567, 88575)
dataPoints(89006, 92685)
dataPoints(92775, 92780)
dataPoints(93142, 93148)
dataPoints(118793, 129721)
dataPoints(200199, 200386)
dataPoints(238682, 238690)
dataPoints(238768, 239176)
dataPoints(239563, 247628)
# dataPoints(247630, 261486)
# dataPoints(261606, 261622)
# dataPoints(261701, 261708)
# dataPoints(261798, 261813)
# dataPoints(262075, 262080)
# dataPoints(287777, 287809)
# dataPoints(288240, 288276)
# dataPoints(288345, 288357)
# dataPoints(288358, 288466)
# dataPoints(288572, 288765)

#print(counter)

# plt.figure(figsize=(8, 5))
# plt.ylabel(abf.sweepLabelY)
# plt.xlabel(abf.sweepLabelX)
# plt.axis([0, 300, -150, 300])
# plt.plot(abf.sweepX, abf.sweepY)
# plt.savefig(filename + '.png')
#plt.show()

#merge()

# from keras.models import Sequential
# from keras.layers import Convolution1D, Dense, Dropout, Flatten, MaxPooling1D
# from keras.utils import np_utils
# import numpy as np
#
# # import your data here instead
# # X - inputs, 10000 samples of 128-dimensional vectors
# # y - labels, 10000 samples of scalars from the set {0, 1, 2}
#
# # X = np.random.rand(10000, 128).astype("float32")
# # y = np.random.randint(3, size=(10000, 1))
#
# X = pd.DataFrame.__array__(pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\1-1 nome and 1 me\19122007_events.csv'))
# Y = pd.DataFrame.__array__(pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\1-1 nome and 1 me\19122007_labels.csv'))
#
# # process the data to fit in a keras CNN properly
# # input data needs to be (N, C, X, Y) - shaped where
# # N - number of samples
# # C - number of channels per sample
# # (X, Y) - sample size
#
# X = X.reshape((36, 1, 1, 1))
#
# # output labels should be one-hot vectors - ie,
# # 0 -> [0, 0, 1]
# # 1 -> [0, 1, 0]
# # 2 -> [1, 0, 0]
# # this operation changes the shape of y from (10000,1) to (10000, 3)
#
# Y = np_utils.to_categorical(Y)
# #
# # # define a CNN
# # # see http://keras.io for API reference
# #
# cnn = Sequential()
# cnn.add(Convolution1D(64, 3,
#                       border_mode="same",
#                       activation="relu",
#                       input_shape=(36, 1, 1)))
# cnn.add(Convolution1D(64, 3, border_mode="same", activation="relu"))
# cnn.add(MaxPooling1D(pool_size=(2, 1)))
#
# cnn.add(Convolution1D(128, 3, border_mode="same", activation="relu"))
# cnn.add(Convolution1D(128, 3, border_mode="same", activation="relu"))
# cnn.add(Convolution1D(128, 3, border_mode="same", activation="relu"))
# cnn.add(MaxPooling1D(pool_size=(2, 1)))
#
# cnn.add(Convolution1D(256, 3, border_mode="same", activation="relu"))
# cnn.add(Convolution1D(256, 3, border_mode="same", activation="relu"))
# cnn.add(Convolution1D(256, 3, border_mode="same", activation="relu"))
# cnn.add(MaxPooling1D(pool_size=(2, 1)))
#
# cnn.add(Flatten())
# cnn.add(Dense(1024, activation="relu"))
# cnn.add(Dropout(0.5))
# cnn.add(Dense(3, activation="softmax"))
#
# # define optimizer and objective, compile cnn
#
# cnn.compile(loss="categorical_crossentropy", optimizer="adam")
#
# # train
#
# cnn.fit(X, y, nb_epoch=20, show_accuracy=True)

# from keras.models import Sequential
# from keras.layers import Convolution1D, Dense, Dropout, Flatten, MaxPooling1D
# from keras.utils import np_utils
# import numpy as np
#
# # import your data here instead
# # X - inputs, 10000 samples of 128-dimensional vectors
# # y - labels, 10000 samples of scalars from the set {0, 1, 2}
#
# X = np.random.rand(10000, 128).astype("float32")
# y = np.random.randint(3, size=(10000, 1))
# # process the data to fit in a keras CNN properly
# # input data needs to be (N, C, X, Y) - shaped where
# # N - number of samples
# # C - number of channels per sample
# # (X, Y) - sample size
#
# X = X.reshape((10000, 128))
#
# # output labels should be one-hot vectors - ie,
# # 0 -> [0, 0, 1]
# # 1 -> [0, 1, 0]
# # 2 -> [1, 0, 0]
# # this operation changes the shape of y from (10000,1) to (10000, 3)
#
# y = np_utils.to_categorical(y)
#
# # define a CNN
# # see http://keras.io for API reference
#
# cnn = Sequential()
# cnn.add(Convolution1D(64, kernel_size=4, strides = 1,
#                       activation="relu",
#                       batch_input_shape=(10000, 1, 128)))
# # cnn.add(Convolution1D(64, 4, strides = 1,  activation="relu"))
# cnn.add(MaxPooling1D(pool_size=1))

# cnn.add(Convolution1D(128, 3,  border_mode="same", activation="relu"))
# cnn.add(Convolution1D(128, 3,  border_mode="same", activation="relu"))
# cnn.add(Convolution1D(128, 3,  border_mode="same", activation="relu"))
# cnn.add(MaxPooling1D(pool_size=2))
#
# cnn.add(Convolution1D(256, 3,  border_mode="same", activation="relu"))
# cnn.add(Convolution1D(256, 3,  border_mode="same", activation="relu"))
# cnn.add(Convolution1D(256, 3,  border_mode="same", activation="relu"))
# cnn.add(MaxPooling1D(pool_size=2))

# cnn.add(Flatten())
# cnn.add(Dense(1024, activation="relu"))
# cnn.add(Dropout(0.5))
# cnn.add(Dense(3, activation="softmax"))
#
# # define optimizer and objective, compile cnn
#
# cnn.compile(loss="categorical_crossentropy", optimizer="adam")
#
# # train
#
# cnn.fit(X, y, epochs=20)

# from keras.models import Sequential
# from keras.layers import Convolution2D, Dense, Dropout, Flatten, MaxPooling2D
# from keras.utils import np_utils
# import numpy as np
#
# # import your data here instead
# # X - inputs, 10000 samples of 128-dimensional vectors
# # y - labels, 10000 samples of scalars from the set {0, 1, 2}
#
# X = np.random.rand(10000, 128).astype("float32")
# y = np.random.randint(3, size=(10000, 1))
# # process the data to fit in a keras CNN properly
# # input data needs to be (N, C, X, Y) - shaped where
# # N - number of samples
# # C - number of channels per sample
# # (X, Y) - sample size
#
# X = X.reshape((10000, 128, 1))
# print(X.shape)
#
# # output labels should be one-hot vectors - ie,
# # 0 -> [0, 0, 1]
# # 1 -> [0, 1, 0]
# # 2 -> [1, 0, 0]
# # this operation changes the shape of y from (10000,1) to (10000, 3)
#
# y = np_utils.to_categorical(y)
#
# # define a CNN
# # see http://keras.io for API reference
#
# cnn = Sequential()
# cnn.add(Convolution2D(2, (1,2), strides = (1,1), data_format= "channels_last",
#                       activation="relu",
#                       input_shape=(1, 1, 128, 1)))
# # cnn.add(Convolution1D(64, 4, strides = 1,  activation="relu"))
# cnn.add(MaxPooling2D(pool_size=(1,1)))
#
# cnn.add(Flatten())
# cnn.add(Dense(1024, activation="relu"))
# cnn.add(Dropout(0.5))
# cnn.add(Dense(3, activation="softmax"))
#
# # define optimizer and objective, compile cnn
#
# cnn.compile(loss="categorical_crossentropy", optimizer="adam")
#
# # train
#
# cnn.fit(X, y, epochs=20)

# import pandas as pd
# df = pd.read_csv(r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\filtered_bessel8pole_500hz_19122007.abf')
# #df['labels'] =df['species'].astype('category').cat.codes
#
# from sklearn.model_selection import train_test_split
# import keras
#
# #X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
# #Y = df['labels']
# x_train, x_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.33, shuffle= True)
#
# # The known number of output classes.
# num_classes = 3
#
# # Input image dimensions
# #input_shape = (4,)
#
# # Convert class vectors to binary class matrices. This uses 1 hot encoding.
# y_train_binary = keras.utils.to_categorical(y_train, num_classes)
# y_test_binary = keras.utils.to_categorical(y_test, num_classes)
#
# x_train = x_train.reshape(10000, 21,1)
# #x_test = x_test.reshape(50, 4,1)
#
# from keras.models import Sequential
# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Flatten, Conv1D
# from keras.callbacks import ModelCheckpoint
# from keras.models import model_from_json
# from keras import backend as K
#
# model = Sequential()
# model.add(Conv1D(32, (3), input_shape=(121,1), activation='relu'))
# model.add(Flatten())
# model.add(Dense(64, activation='softmax'))
# model.add(Dense(num_classes, activation='softmax'))
#
# model.compile(loss=keras.losses.categorical_crossentropy,
#               optimizer=keras.optimizers.Adadelta(),
#               metrics=['accuracy'])
#
# model.summary()
#
# batch_size = 128
# epochs = 10
# model.fit(x_train, y_train_binary,
#           batch_size=batch_size,
#           epochs=epochs,
#           verbose=1,
#           validation_data=(x_test, y_test_binary))
#
# from keras.models import Sequential
# from keras.layers import Convolution2D, Dense, Dropout, Flatten, MaxPooling2D
# from keras.utils import np_utils
# import numpy as np
#
# # import your data here instead
# # X - inputs, 10000 samples of 128-dimensional vectors
# # y - labels, 10000 samples of scalars from the set {0, 1, 2}
#
# X = np.random.rand(10000, 128).astype("float32")
# y = np.random.randint(3, size=(10000, 1))
# # process the data to fit in a keras CNN properly
# # input data needs to be (N, C, X, Y) - shaped where
# # N - number of samples
# # C - number of channels per sample
# # (X, Y) - sample size
#
# X = X.reshape((10000, 128, 1))
# print(X.shape)
#
# # output labels should be one-hot vectors - ie,
# # 0 -> [0, 0, 1]
# # 1 -> [0, 1, 0]
# # 2 -> [1, 0, 0]
# # this operation changes the shape of y from (10000,1) to (10000, 3)
#
# y = np_utils.to_categorical(y)
#
# # define a CNN
# # see http://keras.io for API reference
#
# cnn = Sequential()
# cnn.add(Convolution2D(2, (1,2), strides = (1,1), data_format= "channels_last",
#                       activation="relu",
#                       input_shape=(1, 1, 128, 1)))
# # cnn.add(Convolution1D(64, 4, strides = 1,  activation="relu"))
# cnn.add(MaxPooling2D(pool_size=(1,1)))
#
# cnn.add(Flatten())
# cnn.add(Dense(1024, activation="relu"))
# cnn.add(Dropout(0.5))
# cnn.add(Dense(3, activation="softmax"))
#
# # define optimizer and objective, compile cnn
#
# cnn.compile(loss="categorical_crossentropy", optimizer="adam")
#
# # train
#
# cnn.fit(X, y, epochs=20)

#print(eventLengths)
