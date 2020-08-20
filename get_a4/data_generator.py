from ghost_scan.getData import getFilesData, getPositions, getTensorFromFilepathPng
from .constants import h, w
from .preprocess import preprocess

def getDataGenerator():
  for [filename, positions] in getFilesData():
    rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, keepAlphaChannel=True)
    print(filename)
    X = preprocess(rawX, positions)
    Y = getTensorFromFilepathPng('./data/png/%s' % filename, height=h, width=w)
    yield X, Y

def getSingleEntry(filename):
  positions = getPositions(filename)
  rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, keepAlphaChannel=True)
  X = preprocess(rawX, positions)
  Y = getTensorFromFilepathPng('./data/png/%s' % filename, height=h, width=w)
  return X, Y, rawX
