import os
import tensorflow as tf

from ghost_scan.get_tensor_from_filepath import getTensorFromFilepathPng
from .constants import h, w

def getGroundTruth(filename):
  gradientTensor = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename, h, w)
  [tensorRed, _, _] = tf.split(gradientTensor, 3, axis=3)
  groundTruth = tf.cast(tensorRed == 1, tensorRed.dtype)
  return groundTruth

def getDataGenerator():
  for filename in os.listdir('./data/printed_document'):
    if filename[-4:] != '.png':
      continue
    X = getTensorFromFilepathPng('./data/printed_document/%s' % filename, h, w)
    Y = getGroundTruth(filename)
    yield X, Y, [None]
