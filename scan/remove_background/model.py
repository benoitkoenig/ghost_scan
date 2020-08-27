import segmentation_models as sm
import tensorflow as tf

from .constants import h, w

def getModel(weights=None):
  model = sm.Unet('resnet34', input_shape=(h, w, 3), classes=1, activation='sigmoid', weights=None, encoder_weights=None)
  optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5)
  IoUMetric = sm.metrics.IOUScore(threshold=0.5)
  model.compile(optimizer=optimizer, loss='bce', metrics=[IoUMetric])
  if (weights != None):
    model.load_weights(weights)
  return model
