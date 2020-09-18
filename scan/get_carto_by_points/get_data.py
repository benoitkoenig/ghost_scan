from ghost_scan.scan.get_data import getFilenames, loadSingleUnresizedPngTensor, loadPngTensors
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from ghost_scan.constants import h, w, dirpath
from .constants import batchSize
from .preprocess import preprocessX, preprocessY

def getXY(filenames, folder='training'):
  X = loadPngTensors(['%s/data/%s/printed_document/%s' % (dirpath, folder, f) for f in filenames], h, w)
  X = X[:, :, :, 0:3]
  X = preprocessX(X)
  Y = loadPngTensors(['%s/data/%s/printed_gradient_map/%s' % (dirpath, folder, f) for f in filenames], h, w)
  Y = Y[:, :, :, 0:3]
  Y = preprocessY(Y)
  return X, Y

def getValidationData():
  filenames = getFilenames(folder='validation')
  X, Y = getXY(filenames, folder='validation')
  return X, Y

def getDataGenerator():
  filesLeft = getFilenames()
  while len(filesLeft) != 0:
    batch = filesLeft[:batchSize]
    filesLeft = filesLeft[batchSize:]
    X, Y = getXY(batch)
    yield X, Y

def getFullData(filename):
  rawX = loadSingleUnresizedPngTensor('%s/data/training/printed_document/%s' % (dirpath, filename))
  X, coords = resizeWithCoords(rawX, h, w)
  X = X[:, :, :, 0:3]
  X = preprocessX(X)
  Y = loadSingleUnresizedPngTensor('%s/data/training/printed_gradient_map/%s' % (dirpath, filename))
  Y = Y[:, :, :, 0:3]
  Y, _ = resizeWithCoords(Y, h, w)
  Y = preprocessY(Y)
  return X, Y, rawX, coords
