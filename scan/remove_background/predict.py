import tensorflow as tf

from ghost_scan.constants import h, w, dirpath
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from .model import getModel

class RemoveBackground():
  def __init__(self):
    self.model = getModel(weights='%s/scan/weights/remove_background/weights' % dirpath)

  def predict(self, inputTensor):
    X = inputTensor[:, :, :, 0:3]
    X, [y1, x1, y2, x2] = resizeWithCoords(X, h, w)
    preds = self.model.predict(X, steps=1)
    mask = tf.image.crop_to_bounding_box(preds, y1, x1, y2 - y1, x2 - x1)
    mask = tf.image.resize(mask, inputTensor.shape[1:3])
    mask = mask > 0.5
    mask = tf.cast(mask, inputTensor.dtype)
    output = mask * inputTensor
    return output
