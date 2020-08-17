import tensorflow as tf

from .model import getModel
from .data_generator import getDataGenerator

gen = getDataGenerator()
model = getModel(weights=None)

reduceLrCb = tf.keras.callbacks.ReduceLROnPlateau(monitor='loss', factor=0.2, patience=4, min_lr=4e-6)
loggerCb = tf.keras.callbacks.CSVLogger('./logs/remove_background.csv')

model.fit(gen, steps_per_epoch=10, epochs=40, callbacks=[reduceLrCb, loggerCb])
model.save_weights('./weights/remove_background.h5', overwrite=True)
