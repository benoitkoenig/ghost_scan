import numpy as np

from ghost_scan.constants import dirpath, numberOfPoints
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from .constants import h, w
from .model import getModel
from .postprocess import postprocess

class GetCartoByPoints:
  def __init__(self):
    self.model = getModel(weights='%s/scan/weights/get_carto_by_points/weights' % dirpath)

  def predict(self, inputTensor):
    X, coordsData = resizeWithCoords(inputTensor, h, w)
    mask = (X[:, :, :, 3] == 1).numpy()
    mask = np.repeat(np.expand_dims(mask, axis=-1), numberOfPoints, axis=-1)
    preds = self.model.predict(X, steps=1)
    maskedPreds = mask * preds
    positions = postprocess(maskedPreds[0], coordsData, inputTensor.shape[1:3])
    return positions
