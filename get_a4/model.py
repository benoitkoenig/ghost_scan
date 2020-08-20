from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, InputLayer
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError

from .constants import h, w, inputChannels

def getModel(weights=None):
  model = Sequential()
  model.add(InputLayer(input_shape=(h, w, inputChannels)))
  model.add(Conv2D(2048, 1, 1, padding='same'))
  model.add(Conv2D(2048, 1, 1, padding='same'))
  model.add(Conv2D(3, 1, 1, padding='same'))

  optimizer = Adam(learning_rate=1e-5)

  model.compile(optimizer=optimizer, loss=MeanSquaredError())
  if (weights != None):
    model.load_weights(weights)
  return model
