import tensorflow as tf

from ghost_scan.scan.get_data import getFilenames, loadPngTensors
from ghost_scan.constants import h, w
from .constants import batchSize
from .preprocess import preprocessTrainingOnly

def getXY(filenames):
  X = loadPngTensors(['./data/printed_document/%s' % f for f in filenames], h, w)[:, :, :, 0:3]
  Y = loadPngTensors(['./data/printed_gradient_map/%s' % f for f in filenames], h, w)[:, :, :, 0:3]
  return X, Y

def getDataGenerator():
  filesLeft = getFilenames()
  while len(filesLeft) != 0:
    batch = filesLeft[:batchSize]
    filesLeft = filesLeft[batchSize:]
    X, Y = getXY(batch)
    X = preprocessTrainingOnly(X)
    yield X, Y
