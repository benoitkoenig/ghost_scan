import tensorflow as tf

from ghost_scan.constants import filesCount
from .model import getModel
from .data_generator import getDataGenerator

gen = getDataGenerator()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('./scan/logs/get_carto_by_class.csv')

steps_per_epoch = 10
model.fit(gen, steps_per_epoch=steps_per_epoch, epochs=filesCount // steps_per_epoch, callbacks=[loggerCb])
model.save_weights('./scan/weights/get_carto_by_class/weights', overwrite=True)
