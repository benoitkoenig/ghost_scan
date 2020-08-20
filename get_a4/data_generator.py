from ghost_scan.getData import getFilesData, getPositions, getTensorFromFilepathPng
from .constants import h, w
from .preprocess import preprocess

def getXY(filename, positions):
  print(filename)
  rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, keepAlphaChannel=True)
  X = preprocess(rawX, positions)
  Y = getTensorFromFilepathPng('./data/png/%s' % filename, height=h, width=w)
  return X, Y, rawX

def getDataGenerator():
  for [filename, positions] in getFilesData():
    X, Y, _ = getXY(filename, positions)
    yield X, Y
