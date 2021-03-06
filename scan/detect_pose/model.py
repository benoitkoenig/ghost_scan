import segmentation_models as sm
import tensorflow as tf

from ghost_scan.constants import h, w, numberOfPoints
from .loss import loss, prAsCoeffLoss, actualNearestPixelsMse
from .metrics import bestPredDistance

def getModel(weights=None):
  model = sm.Unet('resnet34', input_shape=(h, w, 4), classes=numberOfPoints, activation='sigmoid', weights=None, encoder_weights=None)
  optimizer = tf.keras.optimizers.Adam(learning_rate=5e-4)
  model.compile(optimizer=optimizer, loss=loss, metrics=[bestPredDistance, prAsCoeffLoss, actualNearestPixelsMse])
  if (weights != None):
    model.load_weights(weights)
  return model
