from ghost_scan.scan.get_data import getFilenames, loadPngTensors
from ghost_scan.constants import h, w, dirpath
from .constants import validationSize, batchSize

def getXY(filenames):
  X = loadPngTensors(['%s/data/printed_document_without_background/%s' % (dirpath, f) for f in filenames], h, w)
  Y = loadPngTensors(['%s/data/printed_gradient_map/%s' % (dirpath, f) for f in filenames], h, w)[:, :, :, 0:3]
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
