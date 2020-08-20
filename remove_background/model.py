import segmentation_models as sm
import tensorflow as tf

from .constants import h, w

def getModel(weights=None):
  model = sm.Unet('resnet34', input_shape=(h, w, 3), classes=1, activation='sigmoid', weights=None, encoder_weights=None)
  optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)
  model.compile(optimizer=optimizer, loss=tf.keras.losses.BinaryCrossentropy())
  return model
