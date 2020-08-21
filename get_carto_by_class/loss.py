import tensorflow as tf

from ghost_scan.constants import numberOfPoints
from .constants import h, w

def loss(gt, pr):
  mask = tf.cast(gt != 0, dtype=pr.dtype)
  maskedPr = mask * pr
  averagePredictedGt = tf.reduce_sum(maskedPr * gt, axis=[0, 1, 2]) / tf.reduce_sum(maskedPr, axis=[0, 1, 2])
  averagePredictedGt = tf.stop_gradient(averagePredictedGt)
  adjustedGt = tf.stop_gradient(gt - averagePredictedGt)
  loss = mask * adjustedGt * (1 - pr) ** 2
  return loss
