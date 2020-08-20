import tensorflow as tf

from .model import getModel
from .data_generator import getDataGenerator

gen = getDataGenerator()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('./logs/get_cartography_by_points.csv')

model.fit(gen, steps_per_epoch=10, epochs=40, callbacks=[loggerCb])
model.save_weights('./weights/get_cartography_by_points', overwrite=True)
