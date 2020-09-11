import numpy as np

from ghost_scan.constants import h, w, numberOfPoints

indexGrid = np.mgrid[0:h, 0:w]
indexGrid = np.transpose(indexGrid, [1, 2, 0])
indexGrid = np.expand_dims(indexGrid, axis=2)
indexGrid = np.repeat(indexGrid, numberOfPoints, axis=-2)
indexGrid = np.reshape(indexGrid, (h * w, numberOfPoints, 2))

def getRawPositions(preds):
  prMaxPerChannel = np.amax(preds, axis=(0, 1))
  pr = (preds > prMaxPerChannel / 10) * preds
  pr = np.expand_dims(pr, axis=-1)
  pr = np.repeat(pr, 2, axis=-1)
  pr = np.reshape(pr, (h * w, numberOfPoints, 2))

  assert pr.shape == indexGrid.shape # == (h * w, numberOfPoints, 2)
  indices = np.sum(pr * indexGrid, axis=0) / np.sum(pr, axis=0)
  return indices

def postprocess(maskedPreds, coords, outputSize):
  [y1, x1, y2, x2] = coords
  [outputH, outputW] = outputSize

  positions = getRawPositions(maskedPreds)
  positions[:, 0] = (positions[:, 0] - y1) / (y2 - y1) * outputH
  positions[:, 1] = (positions[:, 1] - x1) / (x2 - x1) * outputW

  return positions
