from ghost_scan.get_data import getFilesData, getTensorFromFilepathPng
from ghost_scan.preprocess import resize, removeAlphaChannel
from .constants import h, w

def getXY(filename):
  X = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename)
  X, _ = resize(X, h, w)
  Y = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename)
  Y = removeAlphaChannel(Y)
  Y, _ = resize(Y, h, w)
  return X, Y

def getDataGenerator():
  for [filename, _] in getFilesData():
    X, Y = getXY(filename)
    yield X, Y
