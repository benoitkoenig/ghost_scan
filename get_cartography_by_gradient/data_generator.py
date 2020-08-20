from ghost_scan.get_data import getFilesData, getTensorFromFilepathPng
from .constants import h, w

def getXY(filename):
  X = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, h, w, keepAlphaChannel=True)
  Y = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename, h, w)
  return X, Y

def getDataGenerator():
  for [filename, _] in getFilesData():
    X, Y = getXY(filename)
    yield X, Y
