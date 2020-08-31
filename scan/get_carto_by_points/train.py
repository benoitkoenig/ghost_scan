import tensorflow as tf

from ghost_scan.constants import dirpath
from .constants import epochs, steps_per_epoch
from .model import getModel
from .get_data import getDataGenerator, getValidationData

gen = getDataGenerator()
validationData = getValidationData()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('%s/scan/logs/get_carto_by_points.csv' % dirpath)

model.fit(
  gen,
  validation_data=validationData,
  epochs=epochs,
  steps_per_epoch=steps_per_epoch,
  callbacks=[loggerCb]
)
model.save_weights('%s/scan/weights/get_carto_by_points/weights' % dirpath, overwrite=True)
