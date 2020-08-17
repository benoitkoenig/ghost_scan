import os
import tensorflow as tf

from ghost_scan.get_tensor_from_filepath import getTensorFromFilepathPng
from .constants import h, w

def getGroundTruth(filename):
  transparentImageTensor = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, h, w, keepAlphaChannel=True)
  [_, _, _, alphaChannel] = tf.split(transparentImageTensor, 4, axis=3)
  return alphaChannel

def getDataGenerator():
  for filename in os.listdir('./data/printed_document'):
    if filename[-4:] != '.png':
      continue
    X = getTensorFromFilepathPng('./data/printed_document/%s' % filename, h, w)
    Y = getGroundTruth(filename)
    yield X, Y, [None]
