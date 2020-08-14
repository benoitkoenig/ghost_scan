import segmentation_models as sm
import tensorflow as tf

from .constants import h, w

BACKBONE = 'resnet34'
preprocess_input = sm.backbones.get_preprocessing(BACKBONE)

model = sm.Unet(BACKBONE, input_shape=(h, w, 3), classes=3, activation='relu', weights=None)
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)
loss = tf.keras.losses.MeanSquaredError() # TODO: we need a custom loss, that ignores the result for coordinates when out of the paper

model.compile(optimizer=optimizer, loss=loss)
