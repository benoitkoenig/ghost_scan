import numpy as np

from ghost_scan.constants import numberOfPoints
from .constants import h, w

def postprocess(preds, coords, outputSize):
  [y1, x1, y2, x2] = coords
  [outputH, outputW] = outputSize
  flattenPreds = np.reshape(preds, (-1, numberOfPoints))
  flatPositions = np.argmax(flattenPreds, axis=0)
  positions = np.array([[index // w, index % w] for index in flatPositions])
  positions[:, 0] = (positions[:, 0] - y1) / (y2 - y1) * outputH
  positions[:, 1] = (positions[:, 1] - x1) / (x2 - x1) * outputW

  return positions
