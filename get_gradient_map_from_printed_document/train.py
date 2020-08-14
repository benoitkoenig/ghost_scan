from tensorflow.keras.callbacks import CSVLogger, ModelCheckpoint

from .model import model
from .data_generator import getDataGenerator

gen = getDataGenerator()

model.fit(gen, steps_per_epoch=5, epochs=80)
