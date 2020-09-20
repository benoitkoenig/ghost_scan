import tensorflow as tf

from ghost_scan.scan.get_data import getFilenames, loadSingleUnresizedPngTensor, getPositions
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from ghost_scan.constants import h, w, dirpath

from .constants import batchSize
from .get_Y import getY, resizePositions
from .preprocess import preprocessX

def getFullData(filename, folder='training'):
  rawX = loadSingleUnresizedPngTensor('%s/data/%s/printed_document/%s' % (dirpath, folder, filename))
  X, coords = resizeWithCoords(rawX, h, w)
  X = X[:, :, :, 0:3]
  X = preprocessX(X)
  positions = resizePositions(getPositions(filename, folder), coords, rawX.shape)
  Y = getY(positions)
  return X, Y, rawX, coords

def getXY(filenames, folder='training'):
  XY = [getFullData(f, folder) for f in filenames]
  X = tf.concat([xy[0] for xy in XY], axis=0)
  Y = tf.concat([xy[1] for xy in XY], axis=0)
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
