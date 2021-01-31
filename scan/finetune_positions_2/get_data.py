import numpy as np
from scipy.interpolate import griddata
import tensorflow as tf

from .constants import batchSize
from .deviations import generateDeviations, getGradientFromDeviations
from ghost_scan.scan.get_a4.get_a4 import getA4
from ghost_scan.scan.get_data import getFilenames, loadPngTensors, getPositions
from ghost_scan.constants import dirpath, coords

from .constants import h, w

coordsNp = np.array(coords)

def getSingleXY(filename, folder='training'):
  # rawX = loadPngTensors(['%s/data/%s/png/%s' % (dirpath, folder, filename)], h, w)[0, :, :, 0:3]
  rawX = loadPngTensors(['%s/data/training/png/03M31-01.png' % (dirpath)], h, w)[0, :, :, 0:3]
  deviations = np.reshape(generateDeviations(), coordsNp.shape)
  deviatedCoords = coordsNp + 0.1 * deviations
  X = getA4(rawX.numpy(), deviatedCoords * [h, w], h, w)
  gradientDeviations = getGradientFromDeviations(np.reshape(deviations, (5, 5, 2))) # TODO: The shape shouldnt be defined here
  Y = np.reshape(gradientDeviations * 0.5 + 0.5, -1)
  return X, Y, rawX, deviatedCoords

def getXY(filenames, folder='training'):
  XY = [getSingleXY(filename, folder) for filename in filenames]
  X = tf.convert_to_tensor([x for (x, _, _, _) in XY], dtype=tf.float32)
  Y = tf.convert_to_tensor([y for (_, y, _, _) in XY], dtype=tf.float32)
  return X, Y

def getValidationData():
  filenames = getFilenames(folder='validation')
  X, Y = getXY(filenames, folder='validation')
  return X, Y

def getDataGenerator():
  filesLeft = getFilenames()
  while len(filesLeft) != 0:
    batch = filesLeft[:batchSize]
    filesLeft = filesLeft[batchSize:]
    X, Y = getXY(batch)
    yield X, Y
