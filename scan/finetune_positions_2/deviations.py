import numpy as np

from ghost_scan.constants import coords

coordsNp = np.array(coords)

def generateDeviations():
  deviations = np.random.random((5, 5, 2)) - 0.5
  deviations[0, :, 0] = 0
  deviations[4, :, 0] = 0
  deviations[:, 0, 1] = 0
  deviations[:, 4, 1] = 0
  return deviations

def getGradientFromDeviations(deviations):
  deviationsY = deviations[:, :, 0:1]
  gradientsY = np.pad(deviationsY, [(0, 1), (0, 0), (0, 0)]) - np.pad(deviationsY, [(1, 0), (0, 0), (0, 0)])
  gradientsY = np.pad(gradientsY[1:5, :, :], [(0, 1), (0, 0), (0, 0)])

  deviationsX = deviations[:, :, 1:2]
  gradientsX = np.pad(deviationsX, [(0, 0), (0, 1), (0, 0)]) - np.pad(deviationsX, [(0, 0), (1, 0), (0, 0)])
  gradientsX = np.pad(gradientsX[:, 1:5, :], [(0, 0), (0, 1), (0, 0)])

  gradients = np.concatenate([gradientsY, gradientsX], axis=-1)

  return gradients
