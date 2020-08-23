import tensorflow as tf

from ghost_scan.constants import filesCount
from .model import getModel
from .data_generator import getDataGenerator

gen = getDataGenerator()
model = getModel(weights=None)

reduceLrCb = tf.keras.callbacks.ReduceLROnPlateau(monitor='loss', factor=0.2, patience=4, min_lr=4e-6)
loggerCb = tf.keras.callbacks.CSVLogger('./scan/logs/get_carto_by_gradient.csv')

steps_per_epoch = 10
model.fit(gen, steps_per_epoch=steps_per_epoch, epochs=filesCount // steps_per_epoch, callbacks=[reduceLrCb, loggerCb])
model.save_weights('./scan/weights/get_carto_by_gradient.h5/weights', overwrite=True)
