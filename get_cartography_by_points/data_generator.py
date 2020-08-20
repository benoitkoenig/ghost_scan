from ghost_scan.get_data import getFilesData, getTensorFromFilepathPng
from .preprocess import preprocess, preprocessPositions

def getXY(filename, positions):
  rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, keepAlphaChannel=True)
  X, coords = preprocess(rawX)
  Y = preprocessPositions(positions, coords)
  return X, Y, rawX, coords

def getDataGenerator():
  for [filename, positions] in getFilesData():
    X, Y, _, _ = getXY(filename, positions)
    yield X, Y
