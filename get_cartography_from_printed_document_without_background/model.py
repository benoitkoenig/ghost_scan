from tensorflow.keras.layers import Conv2D, Dense, Flatten
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError

from .constants import h, w, numberOfPoints

def getModel():
  model = Sequential()
  model.add(Conv2D(128, 5, 3))
  model.add(Conv2D(128, 5, 3))
  model.add(Conv2D(128, 5, 3))
  model.add(Flatten(name='flatten'))
  model.add(Dense(256, activation='relu', name='relu1'))
  model.add(Dense(numberOfPoints * 2, activation='linear', name='predictions'))

  optimizer = Adam(learning_rate=1e-5)

  model.compile(optimizer=optimizer, loss=MeanSquaredError())
  return model
