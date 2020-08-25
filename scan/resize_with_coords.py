import math
import tensorflow as tf

def resizeWithCoords(inputTensor, height, width):
  downsizedTensor = tf.image.resize(inputTensor, (height, width), preserve_aspect_ratio=True)

  [_, downsizedH, downsizedW, _] = downsizedTensor.shape
  paddingHBefore = (height - downsizedH) // 2
  paddingHAfter = math.ceil((height - downsizedH) / 2)
  paddingWBefore = (width - downsizedW) // 2
  paddingWAfter = math.ceil((width - downsizedW) / 2)
  resizedTensor = tf.pad(downsizedTensor, [(0, 0), (paddingHBefore, paddingHAfter), (paddingWBefore, paddingWAfter), (0, 0)])

  return resizedTensor, [paddingHBefore, paddingWBefore, height - paddingHAfter, width - paddingWAfter]
