import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Dense, Flatten, Input

from ghost_scan.constants import numberOfPoints
from .constants import h, w
from .loss import loss

def getModel(weights=None):
  model = tf.keras.Sequential()
  model.add(Input((h, w, 3)))
  model.add(Conv2D(256, 3, 1, activation='relu'))
  model.add(Conv2D(256, 3, 1, activation='relu'))
  model.add(Conv2D(256, 3, 2, activation='relu'))
  model.add(Conv2D(256, 3, 1, activation='relu'))
  model.add(Conv2D(256, 3, 1, activation='relu'))
  model.add(Conv2D(256, 3, 2, activation='relu'))
  model.add(Conv2D(256, 3, 1, activation='relu'))
  model.add(Conv2D(256, 3, 1, activation='relu'))
  model.add(Conv2D(256, 3, 2, activation='relu'))
  model.add(Conv2D(256, 3, 1, activation='relu'))
  model.add(Conv2D(256, 3, 1, activation='relu'))
  model.add(Conv2D(256, 3, 2, activation='relu'))
  model.add(Flatten())
  model.add(Dense(1024, activation='relu'))
  model.add(Dense(2 * numberOfPoints, activation='linear'))

  optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)
  model.compile(optimizer=optimizer, loss=loss)
  if (weights != None):
    model.load_weights(weights)
  return model
