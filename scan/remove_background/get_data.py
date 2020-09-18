import tensorflow as tf

from ghost_scan.scan.get_data import getFilenames, loadPngTensors
from ghost_scan.constants import h, w, dirpath
from .constants import validationSize, batchSize
from .preprocess import preprocessTrainingOnly

def getXY(filenames):
  X = loadPngTensors(['%s/data/training/printed_document/%s' % (dirpath, f) for f in filenames], h, w)[:, :, :, 0:3]
  Y = loadPngTensors(['%s/data/training/printed_gradient_map/%s' % (dirpath, f) for f in filenames], h, w)[:, :, :, 0:1]
  Y = tf.cast(Y == 1, dtype=X.dtype)
  return X, Y

allFilenames = getFilenames()
validationSet = allFilenames[:validationSize]
trainSet = allFilenames[validationSize:]

def getValidationData():
  X, Y = getXY(validationSet)
  return X, Y

def getDataGenerator():
  filesLeft = [f for f in trainSet]
  while len(filesLeft) != 0:
    batch = filesLeft[:batchSize]
    filesLeft = filesLeft[batchSize:]
    X, Y = getXY(batch)
    X = preprocessTrainingOnly(X)
    yield X, Y
