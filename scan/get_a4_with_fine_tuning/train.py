import tensorflow as tf

from ghost_scan.constants import filesCount
from .model import getModel
from .get_data import getDataGenerator

gen = getDataGenerator()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('./scan/logs/get_a4_with_fine_tuning.csv')

steps_per_epoch = 10
model.fit(gen, steps_per_epoch=steps_per_epoch, epochs=filesCount // steps_per_epoch, callbacks=[loggerCb])
model.save_weights('./scan/weights/get_a4_with_fine_tuning/weights', overwrite=True)
