import tensorflow as tf

from ghost_scan.scan.get_data import getFilenames, loadPngTensors
from ghost_scan.constants import h, w, dirpath
from .constants import batchSize
from .preprocess import preprocessTrainingOnly

def getXY(filenames, folder='training'):
  X = loadPngTensors(['%s/data/%s/printed_document/%s' % (dirpath, folder, f) for f in filenames], h, w)[:, :, :, 0:3]
  Y = loadPngTensors(['%s/data/%s/printed_gradient_map/%s' % (dirpath, folder, f) for f in filenames], h, w)[:, :, :, 0:1]
  Y = tf.cast(Y == 1, dtype=X.dtype)
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
    X = preprocessTrainingOnly(X)
    yield X, Y
