import math
import numpy as np
import os
import PIL
import tensorflow as tf

from .constants import h, w

def resize(inputTensor):
  [_, inputH, inputW, _] = inputTensor.shape
  if (inputH > h) | (inputW > w):
    factor = min(h / inputH, w / inputW)
    newH = int(inputH * factor)
    newW = int(inputW * factor)
    downsizedTensor = tf.image.resize(inputTensor, (newH, newW))
  else:
    downsizedTensor = inputTensor

  [_, downsizedH, downsizedW, _] = downsizedTensor.shape
  paddingHBefore = (h - downsizedH) // 2
  paddingHAfter = math.ceil((h - downsizedH) / 2)
  paddingWBefore = (w - downsizedW) // 2
  paddingWAfter = math.ceil((w - downsizedW) / 2)
  resizedTensor = tf.pad(downsizedTensor, [(0, 0), (paddingHBefore, paddingHAfter), (paddingWBefore, paddingWAfter), (0, 0)])

  return resizedTensor

def getTensorFromFilepathPng(filepath):
  imgRGBA = PIL.Image.open(filepath)
  imgRGB = imgRGBA.convert('RGB')
  data = np.asarray(imgRGB) / 255
  tensor = tf.convert_to_tensor([data])
  resizedTensor = resize(tensor)
  return resizedTensor

def getGroundTruth(filename):
  gradientTensor = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename)
  [tensorRed, _, _] = tf.split(gradientTensor, 3, axis=3)
  groundTruth = tf.cast(tensorRed == 1, tensorRed.dtype)
  return groundTruth

def getDataGenerator():
  for filename in os.listdir('./data/printed_document'):
    if filename[-4:] != '.png':
      continue
    X = getTensorFromFilepathPng('./data/printed_document/%s' % filename)
    Y = getGroundTruth(filename)
    yield X, Y, [None]
