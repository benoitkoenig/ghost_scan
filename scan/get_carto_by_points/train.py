import tensorflow as tf

from .constants import epochs, steps_per_epoch
from .model import getModel
from .get_data import getDataGenerator, getValidationData

gen = getDataGenerator()
validationData = getValidationData()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('./scan/logs/get_carto_by_points.csv')

model.fit(
  gen,
  validation_data=validationData,
  epochs=epochs,
  steps_per_epoch=steps_per_epoch,
  callbacks=[loggerCb]
)
model.save_weights('./scan/weights/get_carto_by_points/weights', overwrite=True)