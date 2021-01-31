import numpy as np

from ghost_scan.constants import coords

coordsNp = np.array(coords)

def generateDeviations():
  deviations = np.random.random((5, 5, 2)) - 0.5
  deviations[0, :, 0] = 0
  deviations[4, :, 0] = 0
  deviations[:, 0, 1] = 0
  deviations[:, 4, 1] = 0
  deviations = np.reshape(deviations, coordsNp.shape)
  return deviations

def getGradientFromDeviations(deviationsInput):
  deviations = np.reshape(deviationsInput, (5, 5, 2))

  deviationsY = deviations[:, :, 0:1]
  gradientsY = np.pad(deviationsY, [(0, 1), (0, 0), (0, 0)]) - np.pad(deviationsY, [(1, 0), (0, 0), (0, 0)])
  gradientsY = gradientsY[0:5, :, :]

  deviationsX = deviations[:, :, 1:2]
  gradientsX = np.pad(deviationsX, [(0, 0), (0, 1), (0, 0)]) - np.pad(deviationsX, [(0, 0), (1, 0), (0, 0)])
  gradientsX = gradientsX[:, 0:5, :]

  gradients = np.concatenate([gradientsY, gradientsX], axis=-1)
  gradients = np.reshape(gradients, coordsNp.shape)
  return gradients

def getDeviationsFromGradients(gradientsInput):
  gradients = np.reshape(gradientsInput, (5, 5, 2))

  gradientsY = gradients[:, :, 0:1]
  deviationsY = np.cumsum(gradientsY, axis=0)

  gradientsX = gradients[:, :, 1:2]
  deviationsX = np.cumsum(gradientsX, axis=1)

  deviations = np.concatenate([deviationsY, deviationsX], axis=-1)
  deviations = np.reshape(deviations, (coordsNp.shape))
  return deviations
