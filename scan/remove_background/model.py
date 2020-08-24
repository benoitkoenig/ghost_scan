import segmentation_models as sm
import tensorflow as tf

from .constants import h, w
from .loss import loss

def getModel(weights=None):
  model = sm.Unet('resnet34', input_shape=(h, w, 3), classes=1, activation='sigmoid', weights=None, encoder_weights=None)
  optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)
  IoUMetric = tf.keras.metrics.MeanIoU(num_classes=2)
  model.compile(optimizer=optimizer, loss=loss, metrics=[IoUMetric])
  if (weights != None):
    model.load_weights(weights)
  return model