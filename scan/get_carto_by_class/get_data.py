from ghost_scan.scan.get_data import getFilesData, getTensorFromFilepathPng
from ghost_scan.scan.preprocess import resize, removeAlphaChannel
from .constants import h, w
from .preprocessY import preprocessY

def getXY(filename):
  rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename)
  X, coords = resize(rawX, h, w)
  Y = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename)
  Y = removeAlphaChannel(Y)
  Y, _ = resize(Y, h, w)
  Y = preprocessY(Y)
  return X, Y, rawX, coords

def getDataGenerator():
  for [filename, _] in getFilesData():
    X, Y, _, _ = getXY(filename)
    yield X, Y
