from ghost_scan.scan.get_data import getFilenames, loadSingleUnresizedPngTensor, loadPngTensors
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from ghost_scan.constants import h, w
from .constants import validationSize, batchSize
from .preprocess import preprocessX, preprocessY

def getXY(filenames):
  X = loadPngTensors(['./data/printed_document/%s' % f for f in filenames], h, w)
  X = X[:, :, :, 0:3]
  X = preprocessX(X)
  Y = loadPngTensors(['./data/printed_gradient_map/%s' % f for f in filenames], h, w)
  Y = Y[:, :, :, 0:3]
  Y = preprocessY(Y)
  return X, Y

allFilenames = getFilenames()
validationSet = allFilenames[:validationSize]
trainSet = allFilenames[validationSize:]

def getValidationData():
  X, Y = getXY(validationSet)
  return X, Y

def getDataGenerator():
  filesLeft = [f for f in trainSet]
  while len(filesLeft) != 0:
    batch = filesLeft[:batchSize]
    filesLeft = filesLeft[batchSize:]
    X, Y = getXY(batch)
    yield X, Y

def getFullData(filename):
  rawX = loadSingleUnresizedPngTensor('./data/printed_document/%s' % filename)
  X, coords = resizeWithCoords(rawX, h, w)
  X = X[:, :, :, 0:3]
  X = preprocessX(X)
  Y = loadSingleUnresizedPngTensor('./data/printed_gradient_map/%s' % filename)
  Y = Y[:, :, :, 0:3]
  Y, _ = resizeWithCoords(Y, h, w)
  Y = preprocessY(Y)
  return X, Y, rawX, coords
