import segmentation_models as sm
import tensorflow as tf

from .constants import h, w

BACKBONE = 'resnet34'
preprocess_input = sm.backbones.get_preprocessing(BACKBONE)
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)
loss = tf.keras.losses.MeanSquaredError() # TODO: use a custom loss where a pred > 1 for a target of 1 is ok

def getModel():
  model = sm.Unet(BACKBONE, input_shape=(h, w, 3), classes=3, activation='relu', weights=None, encoder_weights=None)
  model.compile(optimizer=optimizer, loss=loss)
  return model
