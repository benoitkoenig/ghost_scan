import math
import tensorflow as tf

def resize(inputTensor, height, width):
  [_, inputH, inputW, _] = inputTensor.shape
  if (inputH > height) | (inputW > width):
    factor = min(height / inputH, width / inputW)
    newH = int(inputH * factor)
    newW = int(inputW * factor)
    downsizedTensor = tf.image.resize(inputTensor, (newH, newW))
  else:
    downsizedTensor = inputTensor

  [_, downsizedH, downsizedW, _] = downsizedTensor.shape
  paddingHBefore = (height - downsizedH) // 2
  paddingHAfter = math.ceil((height - downsizedH) / 2)
  paddingWBefore = (width - downsizedW) // 2
  paddingWAfter = math.ceil((width - downsizedW) / 2)
  resizedTensor = tf.pad(downsizedTensor, [(0, 0), (paddingHBefore, paddingHAfter), (paddingWBefore, paddingWAfter), (0, 0)])

  return resizedTensor, [paddingHBefore, paddingWBefore, height - paddingHAfter, width - paddingWAfter]

def removeAlphaChannel(tensor):
  return tensor[:, :, :, 0:3]
