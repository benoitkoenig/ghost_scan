import segmentation_models as sm
import tensorflow as tf

from .constants import h, w
from .loss import loss

def getModel():
  model = sm.Unet('resnet34', input_shape=(h, w, 3), classes=3, activation='linear', weights=None, encoder_weights=None)
  optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)
  model.compile(optimizer=optimizer, loss=loss)
  return model
