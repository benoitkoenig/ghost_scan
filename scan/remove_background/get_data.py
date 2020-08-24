import tensorflow as tf

from ghost_scan.scan.get_data import getFilesData, getTensorFromFilepathPng
from ghost_scan.scan.preprocess import resize, removeAlphaChannel
from .constants import h, w, validationSize, batchSize

def getXY(filename):
  X = getTensorFromFilepathPng('./data/printed_document/%s' % filename)
  X = removeAlphaChannel(X)
  X, _ = resize(X, h, w)
  Y = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename)
  Y, _ = resize(Y, h, w)
  Y = Y[:, :, :, 3]
  return X, Y

def getXYBatch(filenames):
  XY = [getXY(filename) for filename in filenames]
  X = [xy[0] for xy in XY]
  Y = [xy[1] for xy in XY]
  # TODO make all getXY handle arrays of filenames and get rid of getXYBatch and this useless reshape o stack
  X = tf.reshape(tf.stack(X, axis=0), (-1, h, w, 3))
  Y = tf.reshape(tf.stack(Y, axis=0), (-1, h, w))
  return X, Y

allFilenames = [f[0] for f in getFilesData()]
validationSet = allFilenames[:validationSize]
trainSet = allFilenames[validationSize:]

def getValidationData():
  X, Y = getXYBatch(validationSet)
  return X, Y

def getDataGenerator():
  filesLeft = [f for f in trainSet]
  while len(filesLeft) != 0:
    batch = filesLeft[:batchSize]
    filesLeft = filesLeft[batchSize:]
    X, Y = getXYBatch(batch)
    yield X, Y
