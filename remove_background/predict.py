import tensorflow as tf

from ghost_scan.preprocess import resize, removeAlphaChannel

from .model import getModel
from .constants import h, w

def predict(inputTensor):
  X = removeAlphaChannel(inputTensor)
  X, [y1, x1, y2, x2] = resize(X, h, w)
  model = getModel(weights='weights/remove_background')
  preds = model.predict(X, steps=1)
  mask = tf.image.crop_to_bounding_box(preds, y1, x1, y2 - y1, x2 - x1)
  mask = tf.image.resize(mask, inputTensor.shape[1:3])
  mask = mask > 0.5
  mask = tf.cast(mask, inputTensor.dtype)
  output = mask * inputTensor
  return output
