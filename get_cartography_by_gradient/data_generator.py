import math
import numpy as np
import os
import PIL
import tensorflow as tf

from ghost_scan.getData import getTensorFromFilepathPng
from .constants import h, w

def getDataGenerator():
  for filename in os.listdir('./data/printed_document'):
    if filename[-4:] != '.png':
      continue
    X = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, h, w, keepAlphaChannel=True)
    Y = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename, h, w)
    yield X, Y, [None]
