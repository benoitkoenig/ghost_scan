from ghost_scan.scan.get_data import getFilenames, loadPngTensors
from .constants import h, w, validationSize, batchSize

def getXY(filenames):
  X = loadPngTensors(['./data/printed_document_without_background/%s' % f for f in filenames], h, w)
  Y = loadPngTensors(['./data/printed_gradient_map/%s' % f for f in filenames], h, w)[:, :, :, 0:3]
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
