from ghost_scan.getData import getFilesData, getPositions, getTensorFromFilepathPng
from .preprocess import preprocess, preprocessPositions

def getDataGenerator():
  for [filename, positions] in getFilesData():
    rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, keepAlphaChannel=True)
    X, coords = preprocess(rawX)
    Y = preprocessPositions(positions, coords)
    yield X, Y

def getSingleEntry(filename):
  positions = getPositions(filename)
  originalImage = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, keepAlphaChannel=True)
  X, coords = preprocess(originalImage)
  originalPositions = positions
  Y = preprocessPositions(originalPositions, coords)
  return originalImage, originalPositions, X, Y, coords
