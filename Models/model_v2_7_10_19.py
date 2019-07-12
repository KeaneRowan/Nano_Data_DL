import csv
import pandas as pd
from Label_Generation import genLabels

##########version summary



# v2: as of 7/10:
# 250 nome, 250 1me, sample length 10000, batch size: 32, epochs:20, test size = .25

oneme_1 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\1me_Data_Traces\18n12012_events.csv', header=None)
oneme_2 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\1me_Data_Traces\19219003_events.csv', header=None)
oneme_3 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\1me_Data_Traces\19219006_events.csv', header=None)
oneme_4 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\1me_Data_Traces\19219008_events.csv', header=None)
oneme_5 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\1me_Data_Traces\19219009_events.csv', header=None)
oneme_6 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\1me_Data_Traces\19219010_events.csv', header=None)


nome_1 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\nome_Data_Traces\18713001_events.csv', header=None)
nome_2 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\nome_Data_Traces\18717000_events.csv', header=None)
nome_3 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\nome_Data_Traces\18717001_events.csv', header=None)
nome_4 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\nome_Data_Traces\18717002_events.csv', header=None)
nome_5 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\nome_Data_Traces\18717004_events.csv', header=None)
nome_6 = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\nome_Data_Traces\18717010_events.csv', header=None)

oneme_final = pd.concat([oneme_1, oneme_2, oneme_3, oneme_4, oneme_5, oneme_6], ignore_index= True)
nome_final = pd.concat([nome_1, nome_2, nome_3, nome_4, nome_5, nome_6], ignore_index=True)

oneme_final = oneme_final[0:250]
nome_final = nome_final[0:250]

X = pd.concat([nome_final, oneme_final], ignore_index=True)

genLabels(250,500)

import pandas as pd
import keras
import numpy as np
from sklearn.model_selection import train_test_split

Y = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\Models\Dataset_Labels.csv', header = None)
Y = Y[0:500]

x_train, x_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.25, shuffle= True)

# The known number of output classes.
num_classes = 2

# Input image dimensions
#input_shape = (4,)


# Convert class vectors to binary class matrices. This uses 1 hot encoding.
y_train_binary = keras.utils.to_categorical(y_train, num_classes)
y_test_binary = keras.utils.to_categorical(y_test, num_classes)


x_train = x_train.reshape(375, 10000,1)
x_test = x_test.reshape(125, 10000,1)

from keras.models import Sequential
import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv1D
from keras.callbacks import ModelCheckpoint
from keras.models import model_from_json
from keras import backend as K

model = Sequential()
model.add(Conv1D(32, (3), input_shape=(10000,1), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='softmax'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

#model.summary()

batch_size = 16
epochs = 10

model.fit(x_train, y_train_binary,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test_binary))
