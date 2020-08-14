from tensorflow.keras.callbacks import CSVLogger, ModelCheckpoint

from ghost_scan.get_gradient_map_from_printed_document.model import model
from ghost_scan.get_gradient_map_from_printed_document.data_generator import getDataGenerator

gen = getDataGenerator()

model.fit(gen, steps_per_epoch=5, epochs=80)
