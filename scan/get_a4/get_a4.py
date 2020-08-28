import numpy as np

from .constants import h as destinationHeight, w as destinationWidth

def getOrigin(positions, height=destinationHeight, width=destinationWidth):
  'Returns origin Y, originX, of shape (destinationHeight, destinationWidth), the coordinates of the pixels in the origin data'
  [gridY, gridX] = np.mgrid[0:height, 0:width]
  gridY = gridY / height
  gridX = gridX / width
  doubleGridY = np.stack([gridY, gridY], axis=-1)
  doubleGridX = np.stack([gridX, gridX], axis=-1)

  mask1 = (doubleGridY + doubleGridX) < 1
  origin1 = positions[0]
  vectorY1 = positions[2] - positions[0]
  vectorX1 = positions[1] - positions[0]

  mask2 = 1 - mask1
  origin2 = positions[3]
  vectorY2 = positions[1] - positions[3]
  vectorX2 = positions[2] - positions[3]

  output1 = origin1 + doubleGridY * vectorY1 + doubleGridX * vectorX1
  output2 = origin2 + (1 - doubleGridY) * vectorY2 + (1 - doubleGridX) * vectorX2

  originPositions = np.round(mask1 * output1 + mask2 * output2).astype(np.int64)
  [originY, originX] = np.moveaxis(originPositions, 2, 0)
  return originY, originX

def getA4(originData, inputPositions):
  # In this function, origin is the data from the printed document, destination is the a4-format png
  originY, originX = getOrigin(np.array(inputPositions))
  assert (originY.shape == (destinationHeight, destinationWidth)) & (originX.shape == (destinationHeight, destinationWidth))

  originWidth = originData.shape[1]
  flatOriginIndices = (originX + originWidth * originY).flatten()
  flatOriginData = np.reshape(originData[:, :, 0:3], (-1, 3))

  flatDestination = np.take(flatOriginData, flatOriginIndices, axis=0, mode='wrap')
  destinationData = np.reshape(flatDestination, (destinationHeight, destinationWidth, 3))

  return destinationData
