import tensorflow as tf

from ghost_scan.constants import numberOfPoints, h, w

def pixelwiseLoss(gt, pr):
  mean_per_channel = tf.reduce_sum(pr * gt, axis=[1, 2]) / (tf.reduce_sum(pr, axis=[1, 2]) + 1e-7) # 1e-7 is useful when the document is fully out of the picture, which can occasionnaly happen
  mean_per_batch = tf.math.reduce_mean(mean_per_channel)
  return - mean_per_batch

def getTruePixelMask(gt):
  maxGt = tf.reduce_max(gt, axis=[1, 2])
  maxGt = tf.expand_dims(maxGt, 1)
  maxGt = tf.expand_dims(maxGt, 1)
  maxGt = tf.repeat(maxGt, h, axis=1)
  maxGt = tf.repeat(maxGt, w, axis=2)
  truePixelMask = tf.cast(gt == maxGt, dtype=gt.dtype)
  return truePixelMask

def truePixelLoss(gt, pr):
  truePixelMask = getTruePixelMask(gt)
  truePixelPreds = truePixelMask * pr
  truePixelAvgPred = tf.reduce_sum(truePixelPreds) / tf.reduce_sum(truePixelMask)
  truePixelLoss = (1 - truePixelAvgPred) ** 2
  return truePixelLoss

def loss(gt, pr):
  # pixelwise loss is in - pr * log(distance), truepixelLoss is in (1 - pr) ** 2
  return pixelwiseLoss(gt, pr) + 2 * truePixelLoss(gt, pr)
