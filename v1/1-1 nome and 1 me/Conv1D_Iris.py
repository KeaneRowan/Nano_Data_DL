from __future__ import print_function
import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\MachineLearningTutorial\venv\Lib\site-packages\sklearn\datasets\data\iris_6_26.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
df['labels'] =df['species'].astype('category').cat.codes

from sklearn.model_selection import train_test_split
import keras

# X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
# Y = df['labels']

X = df[df.columns[0:4]]
Y = df[df.columns[4]]

x_train, x_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.33, shuffle= True)

# The known number of output classes.
num_classes = 3

# Input image dimensions
input_shape = (4,)

# Convert class vectors to binary class matrices. This uses 1 hot encoding.
y_train_binary = keras.utils.to_categorical(y_train, num_classes)
y_test_binary = keras.utils.to_categorical(y_test, num_classes)

print("Y TRAIN")
print()
print(y_train_binary)
print()
print("Y TEST")
print()
print(y_test_binary)

# x_train = x_train.reshape(100, 4,1)
# x_test = x_test.reshape(50, 4,1)
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
# model.add(Conv1D(32, (3), input_shape=(4,1), activation='relu'))
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
