import tensorflow as tf

from .constants import epochs, steps_per_epoch
from .model import getModel
from .get_data import getDataGenerator, getValidationData

gen = getDataGenerator()
validationData = getValidationData()
model = getModel(weights=None)

reduceLrCb = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=1e-6)
loggerCb = tf.keras.callbacks.CSVLogger('./scan/logs/remove_background.csv')

model.fit(
  gen,
  validation_data=validationData,
  epochs=epochs,
  steps_per_epoch=steps_per_epoch,
  callbacks=[reduceLrCb, loggerCb]
)
model.save_weights('./scan/weights/remove_background/weights', overwrite=True)
