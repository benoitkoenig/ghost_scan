from ghost_scan.get_data import getFilesData, getPositions, getTensorFromFilepathPng
from ghost_scan.preprocess import resize, removeAlphaChannel
from .constants import h, w
from .preprocess import preprocess

def getXY(filename, positions):
  rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename)
  X = preprocess(rawX, positions)
  Y = getTensorFromFilepathPng('./data/png/%s' % filename)
  Y = removeAlphaChannel(Y)
  Y, _ = resize(Y, h, w)
  return X, Y

def getDataGenerator():
  for [filename, positions] in getFilesData():
    X, Y = getXY(filename, positions)
    yield X, Y
