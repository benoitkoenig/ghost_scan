import tensorflow as tf

from ghost_scan.scan.get_data import getFilesData, getPositions, getTensorFromFilepathPng
from ghost_scan.scan.preprocess import resize
from .constants import h, w
from .preprocess import preprocess

def getXY(filename, positions):
  rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename)
  X = preprocess(rawX, positions)
  Y = getTensorFromFilepathPng('./data/png/%s' % filename)
  Y = Y[:, :, :, 0:3]
  Y = tf.image.resize(Y, (h, w), method='area')
  return X, Y

def getDataGenerator():
  for [filename, positions] in getFilesData():
    X, Y = getXY(filename, positions)
    yield X, Y
