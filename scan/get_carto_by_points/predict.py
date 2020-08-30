import numpy as np

from ghost_scan.constants import numberOfPoints
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from .constants import h, w
from .model import getModel
from .postprocess import postprocess

def predict(inputTensor):
  X, coordsData = resizeWithCoords(inputTensor, h, w)
  mask = (X[:, :, :, 3] == 1).numpy()
  mask = np.repeat(np.expand_dims(mask, axis=-1), numberOfPoints, axis=-1)
  model = getModel(weights='./scan/weights/get_carto_by_points/weights')
  preds = model.predict(X, steps=1)
  maskedPreds = mask * preds
  positions = postprocess(maskedPreds, coordsData, inputTensor.shape[1:3])
  return positions
