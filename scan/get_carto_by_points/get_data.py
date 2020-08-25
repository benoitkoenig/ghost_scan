from ghost_scan.scan.get_data import getFilesData, loadSingleUnresizedPngTensor
from .preprocess import preprocess, preprocessPositions

def getXY(filename, positions):
  rawX = loadSingleUnresizedPngTensor('./data/printed_document_without_background/%s' % filename)
  X, coords = preprocess(rawX)
  Y = preprocessPositions(positions, coords)
  return X, Y, rawX, coords

def getDataGenerator():
  for [filename, positions] in getFilesData():
    X, Y, _, _ = getXY(filename, positions)
    yield X, Y
