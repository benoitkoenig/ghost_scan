import numpy as np

from ghost_scan.constants import coords

coordsNp = np.array(coords)

def generateDeviations():
  rawDeviations = np.random.random(coordsNp.shape)
  deviatedCoords = np.clip(coordsNp + 0.1 * (rawDeviations - 0.5), 0, 1)
  deviations = 10 * (deviatedCoords - coordsNp) + 0.5 # Include the np.clip
  return deviations

def getGradientFromDeviations(deviations):
  deviationsY = deviations[:, :, 0:1]
  deviationsY = np.pad(deviationsY, [(0, 1), (0, 0), (0, 0)]) - np.pad(deviationsY, [(1, 0), (0, 0), (0, 0)])
  deviationsY = np.pad(deviationsY[1:5, :, :], [(0, 1), (0, 0), (0, 0)])

  deviationsX = deviations[:, :, 1:2]
  deviationsX = np.pad(deviationsX, [(0, 0), (0, 1), (0, 0)]) - np.pad(deviationsX, [(0, 0), (1, 0), (0, 0)])
  deviationsX = np.pad(deviationsX[:, 1:5, :], [(0, 0), (0, 1), (0, 0)])

  gradDeviations = np.concatenate([deviationsY, deviationsX], axis=-1)

  return gradDeviations
