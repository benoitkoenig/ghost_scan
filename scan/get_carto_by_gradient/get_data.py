from ghost_scan.scan.get_data import getFilenames, loadPngTensors
from .constants import h, w

def getXY(filenames):
  X = loadPngTensors(['./data/printed_document_without_background/%s' % f for f in filenames], h, w)
  Y = loadPngTensors(['./data/printed_gradient_map/%s' % f for f in filenames], h, w)[:, :, :, 0:3]
  return X, Y

def getDataGenerator():
  for filename in getFilenames():
    X, Y = getXY([filename])
    yield X, Y
