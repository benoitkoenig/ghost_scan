from ghost_scan.scan.get_data import getFilenames, loadSingleUnresizedPngTensor, loadPngTensors
from ghost_scan.scan.resize_with_coords import resizeWithCoords
from .constants import h, w
from .preprocessY import preprocessY

def getFullData(filename):
  rawX = loadSingleUnresizedPngTensor('./data/printed_document_without_background/%s' % filename)
  X, coords = resizeWithCoords(rawX, h, w)
  Y = loadSingleUnresizedPngTensor('./data/printed_gradient_map/%s' % filename)
  Y = Y[:, :, :, 0:3]
  Y, _ = resizeWithCoords(Y, h, w)
  Y = preprocessY(Y)
  return X, Y, rawX, coords

def getXY(filenames):
  X = loadPngTensors(['./data/printed_document_without_background/%s' % f for f in filenames], h, w)
  Y = preprocessY(loadPngTensors(['./data/printed_gradient_map/%s' % f for f in filenames], h, w)[:, :, :, 0:3])
  return X, Y

def getDataGenerator():
  for filename in getFilenames():
    X, Y = getXY([filename])
    yield X, Y
