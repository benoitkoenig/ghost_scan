import math
import numpy as np
import PIL
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

  return resizedTensor

def getTensorFromFilepathPng(filepath, height=None, width=None, keepAlphaChannel=False):
  img = PIL.Image.open(filepath)
  if (keepAlphaChannel == False):
    img = img.convert('RGB')
  data = np.asarray(img) / 255
  tensor = tf.convert_to_tensor([data])
  if (height != None) & (width != None):
    tensor = resize(tensor, height, width)
  return tensor
