import numpy as np
from scipy.interpolate import griddata
import tensorflow as tf

from .constants import batchSize
from ghost_scan.scan.get_a4.get_a4 import getA4
from ghost_scan.scan.get_data import getFilenames, loadSingleUnresizedPngTensor, getPositions
from ghost_scan.constants import dirpath, coords

from .constants import h, w

coordsNp = np.array(coords)

def getSingleXY(filename, folder='training'):
  rawX = loadSingleUnresizedPngTensor('%s/data/%s/printed_document/%s' % (dirpath, folder, filename))[0, :, :, 0:3]
  positions = np.array(getPositions(filename, folder))
  deviations = np.random.uniform(-.05, .05, coordsNp.shape)
  deviatedCoords = np.clip(coordsNp + deviations, 0, 1)
  deviatedPositions = griddata(coordsNp, positions, deviatedCoords, method='linear')
  X = getA4(rawX.numpy(), deviatedPositions, h, w)
  Y = np.reshape(-deviations, -1)
  return X, Y, rawX, deviatedPositions, positions, deviatedCoords

def getXY(filenames, folder='training'):
  XY = [getSingleXY(filename, folder) for filename in filenames]
  X = tf.convert_to_tensor([x for (x, _, _, _, _, _) in XY], dtype=tf.float32)
  Y = tf.convert_to_tensor([y for (_, y, _, _, _, _) in XY], dtype=tf.float32)
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
