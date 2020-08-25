from ghost_scan.scan.get_data import getFilesData, getTensorFromFilepathPng, loadPngTensors
from ghost_scan.scan.preprocess import resize
from .constants import h, w
from .preprocessY import preprocessY

def getFullData(filename):
  rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename)
  X, coords = resize(rawX, h, w)
  Y = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename)
  Y = Y[:, :, :, 0:3]
  Y, _ = resize(Y, h, w)
  Y = preprocessY(Y)
  return X, Y, rawX, coords

def getXY(filenames):
  X = loadPngTensors(['./data/printed_document_without_background/%s' % f for f in filenames], h, w)
  Y = preprocessY(loadPngTensors(['./data/printed_gradient_map/%s' % f for f in filenames], h, w)[:, :, :, 0:3])
  return X, Y

def getDataGenerator():
  for [filename, _] in getFilesData():
    X, Y = getXY([filename])
    yield X, Y
