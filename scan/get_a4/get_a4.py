import numpy as np
from scipy.interpolate import griddata

from ghost_scan.constants import coords
from .constants import h as defaultHeight, w as defaultWidth

def getA4(originData, positions, destinationHeight=defaultHeight, destinationWidth=defaultWidth):
  a4PixelsGrid = np.transpose(np.mgrid[0:destinationHeight, 0:destinationWidth], [1, 2, 0]) / [destinationHeight, destinationWidth]
  origin = griddata(coords, positions, a4PixelsGrid, method='linear')
  origin = np.round(origin).astype(np.int64)
  [originY, originX] = np.transpose(origin, [2, 0, 1])

  assert (originY.shape == (destinationHeight, destinationWidth)) & (originX.shape == (destinationHeight, destinationWidth))

  originWidth = originData.shape[1]
  flatOriginIndices = (originX + originWidth * originY).flatten()
  flatOriginData = np.reshape(originData[:, :, 0:3], (-1, 3))

  flatDestination = np.take(flatOriginData, flatOriginIndices, axis=0, mode='wrap')
  destinationData = np.reshape(flatDestination, (destinationHeight, destinationWidth, 3))

  return destinationData
