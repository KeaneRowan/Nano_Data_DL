from DataSheet_Read import dataPoints as dp


abfFile = r'C:\Users\Elijah\Documents\NanoporeData\abfRaw\19219008.abf'
dataSheet = r'C:\Users\Elijah\Documents\NanoporeData\abfSheets\1me\19219008.xls'
eventFile = '19219008_events.csv'

dp(abfFile, dataSheet, eventFile)

# import pandas as pd
# import numpy as np
#
# X = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\1me_Data_Traces\19219008_events.csv', header=None)
# Y = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v1\1-1 nome and 1 me\19122007_labels.csv', header = None)
#
# from sklearn.model_selection import train_test_split
# import keras
#
# # X = df[df.columns[0:4]]
# # Y = df[df.columns[4]]
#
# print("X")
# print()
# print(X)
# print()
# print("Y")
# print()
# print(Y)
# print()
# x_train, x_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.25, shuffle= True)
#
# # The known number of output classes.
# num_classes = 3
#
# # Input image dimensions
# #input_shape = (4,)
#
#
# #as of 6/26/19, 10 rows, 5 col
# # Convert class vectors to binary class matrices. This uses 1 hot encoding.
# y_train_binary = keras.utils.to_categorical(y_train, num_classes)
# y_test_binary = keras.utils.to_categorical(y_test, num_classes)
#
# x_train = x_train.reshape(15, 1000,1)
# x_test = x_test.reshape(5, 1000,1)
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
# model.add(Conv1D(32, (3), input_shape=(1000,1), activation='relu'))
# model.add(Flatten())
# model.add(Dense(64, activation='softmax'))
# model.add(Dense(num_classes, activation='softmax'))
#
# model.compile(loss=keras.losses.categorical_crossentropy,
#               optimizer=keras.optimizers.Adadelta(),
#               metrics=['accuracy'])
#
# #model.summary()
#
# batch_size = 16
# epochs = 10
# model.fit(x_train, y_train_binary,
#           batch_size=batch_size,
#           epochs=epochs,
#           verbose=1,
#           validation_data=(x_test, y_test_binary))
