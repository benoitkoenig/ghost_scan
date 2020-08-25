import tensorflow as tf

from ghost_scan.scan.preprocess import resize

from .model import getModel
from .constants import h, w

def predict(inputTensor):
  X = inputTensor[:, :, :, 0:3]
  X, [y1, x1, y2, x2] = resize(X, h, w)
  model = getModel(weights='./scan/weights/remove_background/weights')
  preds = model.predict(X, steps=1)
  mask = tf.image.crop_to_bounding_box(preds, y1, x1, y2 - y1, x2 - x1)
  mask = tf.image.resize(mask, inputTensor.shape[1:3])
  mask = mask > 0.5
  mask = tf.cast(mask, inputTensor.dtype)
  output = mask * inputTensor
  return output
