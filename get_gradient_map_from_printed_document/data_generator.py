import math
import numpy as np
import os
import PIL
import tensorflow as tf

from .constants import h, w
from .model import preprocess_input

def getTensorFromFilepathPng(filepath):
  imgRGBA = PIL.Image.open(filepath)
  imgRGB = imgRGBA.convert('RGB')
  data = np.asarray(imgRGB) / 255
  tensor = tf.convert_to_tensor([data])
  resizedTensor = tf.image.resize(tensor, (h, w)) # TODO: adding padding would probably improve the result, though downsizing helps with performance, allowing for faster iterations
  return resizedTensor

def getDataGenerator():
  for filename in os.listdir('./data/printed_document'):
    if filename[-4:] != '.png':
      continue
    X = getTensorFromFilepathPng('./data/printed_document/%s' % filename)
    Y = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename)
    yield preprocess_input(X), Y
