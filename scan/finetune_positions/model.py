import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Dense, Flatten, Input

from ghost_scan.constants import numberOfPoints
from .constants import h, w

def getModel(weights=None):
  model = tf.keras.Sequential()
  model.add(Input((h, w, 3)))
  model.add(Conv2D(256, 5, 2, activation=tf.keras.layers.LeakyReLU(alpha=0.1)))
  model.add(Conv2D(256, 5, 2, activation=tf.keras.layers.LeakyReLU(alpha=0.1)))
  model.add(Conv2D(256, 5, 2, activation=tf.keras.layers.LeakyReLU(alpha=0.1)))
  model.add(Flatten())
  model.add(Dense(1024, activation=tf.keras.layers.LeakyReLU(alpha=0.1)))
  model.add(Dense(2 * numberOfPoints, activation='sigmoid'))

  optimizer = tf.keras.optimizers.Adam(learning_rate=1e-5)
  model.compile(optimizer=optimizer, loss='mse')
  if (weights != None):
    model.load_weights(weights)
  return model
