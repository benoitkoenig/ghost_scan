from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, InputLayer
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError

from ghost_scan.constants import numberOfPoints
from .constants import h, w

def getModel():
  model = Sequential()
  model.add(InputLayer(input_shape=(h, w, 4)))
  model.add(Conv2D(128, 3, 2))
  model.add(Conv2D(128, 3, 2))
  model.add(Conv2D(128, 3, 2))
  model.add(Dropout(0.5))
  model.add(Conv2D(256, 3, 2))
  model.add(Conv2D(256, 3, 2))
  model.add(Conv2D(256, 3, 2))
  model.add(Flatten(name='flatten'))
  model.add(Dense(2048, activation='relu', name='relu1'))
  model.add(Dense(2048, activation='relu', name='relu2'))
  model.add(Dense(numberOfPoints * 2, activation='linear', name='predictions'))

  optimizer = Adam(learning_rate=1e-5)

  model.compile(optimizer=optimizer, loss=MeanSquaredError())
  return model
