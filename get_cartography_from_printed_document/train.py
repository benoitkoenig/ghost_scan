import tensorflow as tf

from .model import getModel
from .data_generator import getDataGenerator

gen = getDataGenerator()
model = getModel()

reduceLrCb = tf.keras.callbacks.ReduceLROnPlateau(monitor='loss', factor=0.2, patience=5, min_lr=4e-7)
loggerCb = tf.keras.callbacks.CSVLogger('./logs/get_cartography_from_printed_document.csv')

model.fit(gen, steps_per_epoch=10, epochs=40, callbacks=[loggerCb, reduceLrCb])
model.save_weights('./weights/get_cartography_from_printed_document', overwrite=True)
