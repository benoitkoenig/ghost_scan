import tensorflow as tf

from ghost_scan.constants import numberOfPoints

def loss(gt, pr):
  mask = tf.cast(gt != 0, dtype=pr.dtype)
  maskedPr = mask * pr
  averages = tf.reduce_sum(maskedPr * gt, axis=[1, 2, 3]) / tf.reduce_sum(maskedPr, axis=[1, 2, 3])
  prod_mean = tf.math.pow(tf.reduce_prod(averages), 1 / numberOfPoints)
  return 1 - prod_mean
