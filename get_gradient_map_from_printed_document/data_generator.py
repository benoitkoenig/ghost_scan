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
  data = np.asarray(imgRGB) / 256
  tensor = tf.convert_to_tensor([data])
  resizedTensor = tf.image.resize(tensor, (h, w)) # TODO: adding padding would probably improve the result, though downsizing helps with performance, allowing for faster iterations
  preprocessedTensor = preprocess_input(resizedTensor)
  return preprocessedTensor

def getDataGenerator():
  for filename in os.listdir('./data/printed_document'):
    X = getTensorFromFilepathPng('./data/printed_document/%s' % filename)
    Y = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename)
    yield X, Y
