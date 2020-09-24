import numpy as np

from ghost_scan.constants import h, w, dirpath
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from .model import getModel

class RemoveBackground():
  def __init__(self):
    self.model = getModel(weights='%s/scan/models/weights/remove_background/weights' % dirpath)

  def predict(self, inputTensor):
    X, coords = resizeWithCoords(inputTensor, h, w)
    X = X[:, :, :, 0:3]
    preds = self.model.predict(X, steps=1)
    output = np.concatenate([X, preds], axis=-1)
    return output, coords
