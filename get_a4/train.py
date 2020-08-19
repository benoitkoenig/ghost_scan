import tensorflow as tf

from .model import getModel
from .data_generator import getDataGenerator

gen = getDataGenerator()
model = getModel()

loggerCb = tf.keras.callbacks.CSVLogger('./logs/get_a4.csv')

model.fit(gen, steps_per_epoch=10, epochs=3, callbacks=[loggerCb])
model.save_weights('./weights/get_a4', overwrite=True)
