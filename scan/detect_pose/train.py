import tensorflow as tf

from ghost_scan.constants import dirpath
from .constants import epochs, steps_per_epoch
from .model import getModel
from .get_data import getDataGenerator, getValidationData

gen = getDataGenerator()
validationData = getValidationData()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('%s/scan/logs/detect_pose.csv' % dirpath)
lrSchedulerCb = tf.keras.callbacks.LearningRateScheduler(lambda epoch: 5e-4 if epoch < 550 else 5e-5)

model.fit(
  gen,
  validation_data=validationData,
  epochs=epochs,
  steps_per_epoch=steps_per_epoch,
  callbacks=[loggerCb, lrSchedulerCb]
)
model.save_weights('%s/scan/models/weights/detect_pose/weights' % dirpath, overwrite=True)
