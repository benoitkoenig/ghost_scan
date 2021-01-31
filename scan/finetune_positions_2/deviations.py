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
  gradientsY = gradientsY[0:5, :, :]

  deviationsX = deviations[:, :, 1:2]
  gradientsX = np.pad(deviationsX, [(0, 0), (0, 1), (0, 0)]) - np.pad(deviationsX, [(0, 0), (1, 0), (0, 0)])
  gradientsX = gradientsX[:, 0:5, :]

  gradients = np.concatenate([gradientsY, gradientsX], axis=-1)

  return gradients

def getDeviationsFromGradients(gradients):
  gradientsY = gradients[:, :, 0:1]
  deviationsY = np.cumsum(gradientsY, axis=0)

  gradientsX = gradients[:, :, 1:2]
  deviationsX = np.cumsum(gradientsX, axis=1)

  deviations = np.concatenate([deviationsY, deviationsX], axis=-1)
  return deviations
