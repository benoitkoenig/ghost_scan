import segmentation_models as sm
import tensorflow as tf

from ghost_scan.constants import numberOfPoints
from .constants import h, w
from .loss import loss
from .metrics import distance

def getModel(weights=None):
  model = sm.Unet('resnet34', input_shape=(h, w, 4), classes=numberOfPoints, activation='sigmoid', weights=None, encoder_weights=None)
  optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)
  model.compile(optimizer=optimizer, loss=loss, metrics=[distance])
  if (weights != None):
    model.load_weights(weights)
  return model
