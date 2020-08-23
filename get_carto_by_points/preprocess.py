import math
import numpy as np
import tensorflow as tf

from ghost_scan.constants import numberOfPoints
from .constants import h, w

def getPaddingSize(inputArray, axis):
  'Get the padding size formed by areas of zero along the given axis'
  sumAlongAxis = np.sum(inputArray, axis)
  relevantElements = np.argwhere(sumAlongAxis != 0)

  zerosBefore = relevantElements[0, 0]
  zerosAfter = relevantElements[-1, 0]
  return (zerosBefore, zerosAfter)

def getRelevantAreaCoords(inputData):
  alphaChannel = inputData[0, :, :, 3]
  (y1, y2) = getPaddingSize(alphaChannel, axis=1)
  (x1, x2) = getPaddingSize(alphaChannel, axis=0)

  return (y1, x1, y2, x2)

def preprocess(inputTensor):
  (y1, x1, y2, x2) = getRelevantAreaCoords(inputTensor.numpy())
  croppedImage = tf.image.crop_to_bounding_box(inputTensor, y1, x1, y2 - y1 + 1, x2 - x1 + 1)
  X = tf.image.resize(croppedImage, (h, w))

  return X, [y1, x1, y2, x2]

def preprocessPositions(inputPositions, coords):
  [y1, x1, y2, x2] = coords
  positions = np.array(inputPositions, dtype=np.float32)
  positions[:, 0] = (positions[:, 0] - y1) / (y2 - y1)
  positions[:, 1] = (positions[:, 1] - x1) / (x2 - x1)
  Y = tf.convert_to_tensor([positions.flatten()])
  return Y

def postprocessPositions(preds, coords):
  [y1, x1, y2, x2] = coords
  positions = np.reshape(np.copy(preds[0]), (numberOfPoints, 2))
  positions[:, 0] = (positions[:, 0] * (y2 - y1)) + y1
  positions[:, 1] = (positions[:, 1] * (x2 - x1)) + x1
  return positions
