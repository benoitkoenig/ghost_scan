from ghost_scan.constants import h, w, dirpath
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from .model import getModel

class RemoveBackground():
  def __init__(self):
    self.model = getModel(weights='%s/scan/weights/remove_background/weights' % dirpath)

  def predict(self, inputTensor):
    X, coords = resizeWithCoords(inputTensor, h, w)
    preds = self.model.predict(X[:, :, :, 0:3], steps=1)
    output = (preds > 0.5) * X
    return output, coords
