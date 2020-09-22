import tensorflow as tf

from ghost_scan.constants import numberOfPoints, h, w

def prAsCoeff(gt, pr):
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

def bceLoss(gt, pr):
  truePixelMask = getTruePixelMask(gt)
  loss0 = - (1 - truePixelMask) * tf.math.log(pr + 1e-7)
  lossMean0 = tf.math.reduce_sum(loss0) / tf.math.reduce_sum(1 - truePixelMask)
  loss1 = - truePixelMask * tf.math.log(1 - pr + 1e-7)
  lossMean1 = tf.math.reduce_sum(loss1) / tf.math.reduce_sum(truePixelMask)
  loss = (lossMean0 + lossMean1) / 2
  return loss

def loss(gt, pr):
  # prAsCoeff loss is in +log(distance), bceLoss is in -log(pr)
  return prAsCoeff(gt, pr) + 0.2 * bceLoss(gt, pr)
