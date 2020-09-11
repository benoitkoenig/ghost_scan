import tensorflow as tf

from ghost_scan.constants import dirpath
from .constants import epochs, steps_per_epoch
from .model import getModel
from .get_data import getDataGenerator

gen = getDataGenerator()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('%s/scan/logs/get_gradient_map.csv' % dirpath)

model.fit(
  gen,
  epochs=epochs,
  steps_per_epoch=steps_per_epoch,
  callbacks=[loggerCb]
)
model.save_weights('%s/scan/weights/get_gradient_map/weights' % dirpath, overwrite=True)
