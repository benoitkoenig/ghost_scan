import tensorflow as tf

from .constants import epochs, steps_per_epoch
from .model import getModel
from .get_data import getDataGenerator

gen = getDataGenerator()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('./scan/logs/get_carto_by_gradient.csv')

model.fit(
  gen,
  epochs=epochs,
  steps_per_epoch=steps_per_epoch,
  callbacks=[loggerCb]
)
model.save_weights('./scan/weights/get_carto_by_gradient/weights', overwrite=True)
