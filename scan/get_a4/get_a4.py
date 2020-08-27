import numpy as np

from .constants import h, w

def getOrigin(positions, h=h, w=w):
  'Returns two numpy arrays, originY and originX, of shape (h, w) that contains, for each pixel in the output, the pixel s coordinates in the input'
  [gridY, gridX] = np.mgrid[0:h, 0:w]
  gridY = gridY.astype(np.float32) / h
  gridX = gridX.astype(np.float32) / w

  mask1 = (gridY + gridX) < 1
  mask1 = np.stack([mask1, mask1], axis=-1)
  origin1 = positions[0]
  vectorY1 = positions[2] - positions[0]
  vectorX1 = positions[1] - positions[0]

  mask2 = 1 - mask1
  origin2 = positions[3]
  vectorY2 = positions[1] - positions[3]
  vectorX2 = positions[2] - positions[3]

  doubleGridY = np.stack([gridY, gridY], axis=-1)
  doubleGridX = np.stack([gridX, gridX], axis=-1)

  output1 = origin1 + doubleGridY * vectorY1 + doubleGridX * vectorX1
  output2 = origin2 + (1 - doubleGridY) * vectorY2 + (1 - doubleGridX) * vectorX2

  originPositions = np.round(mask1 * output1 + mask2 * output2).astype(np.int64)
  [originY, originX] = np.moveaxis(originPositions, 2, 0)
  return originY, originX

def getA4(inputData, inputPositions):
  positions = np.array(inputPositions, dtype=np.float32)
  originY, originX = getOrigin(positions)

  data = inputData[:, :, 0:3]
  flatOriginIndices = (originX + data.shape[1] * originY).flatten()
  flatData = np.reshape(data, (-1, 3))

  flatDestinationChannel0 = np.take(flatData[:, 0], flatOriginIndices)
  flatDestinationChannel1 = np.take(flatData[:, 1], flatOriginIndices)
  flatDestinationChannel2 = np.take(flatData[:, 2], flatOriginIndices)
  flatDestination = np.stack([flatDestinationChannel0, flatDestinationChannel1, flatDestinationChannel2], axis=-1)
  destination = np.reshape(flatDestination, (h, w, 3))

  return destination
