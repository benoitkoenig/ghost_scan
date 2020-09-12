import tensorflow as tf

from ghost_scan.constants import dirpath
from .constants import epochs, steps_per_epoch
from .model import getModel
from .get_data import getDataGenerator, getValidationData

gen = getDataGenerator()
validationData = getValidationData()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('%s/scan/logs/remove_background.csv' % dirpath)
lrCb = tf.keras.callbacks.LearningRateScheduler(lambda epoch: 1e-4 if epoch < 200 else 1e-5)

model.fit(
  gen,
  validation_data=validationData,
  epochs=epochs,
  steps_per_epoch=steps_per_epoch,
  callbacks=[loggerCb, lrCb]
)
model.save_weights('%s/scan/weights/remove_background/weights' % dirpath, overwrite=True)
