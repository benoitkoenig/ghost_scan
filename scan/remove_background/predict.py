import tensorflow as tf

from ghost_scan.constants import dirpath
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from .model import getModel
from .constants import h, w

def predict(inputTensor):
  X = inputTensor[:, :, :, 0:3]
  X, [y1, x1, y2, x2] = resizeWithCoords(X, h, w)
  model = getModel(weights='%s/scan/weights/remove_background/weights' % dirpath)
  preds = model.predict(X, steps=1)
  mask = tf.image.crop_to_bounding_box(preds, y1, x1, y2 - y1, x2 - x1)
  mask = tf.image.resize(mask, inputTensor.shape[1:3])
  mask = mask > 0.5
  mask = tf.cast(mask, inputTensor.dtype)
  output = mask * inputTensor
  return output
