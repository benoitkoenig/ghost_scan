import tensorflow as tf

from .model import getModel
from .data_generator import getDataGenerator

gen = getDataGenerator()
model = getModel(weights=None)

loggerCb = tf.keras.callbacks.CSVLogger('./logs/get_carto_by_class.csv')

model.fit(gen, steps_per_epoch=10, epochs=40, callbacks=[loggerCb])
model.save_weights('./weights/get_carto_by_class', overwrite=True)
