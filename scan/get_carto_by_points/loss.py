import tensorflow as tf

from ghost_scan.constants import numberOfPoints

def loss(gt, pr):
  mask = tf.cast(gt != 0, dtype=pr.dtype)
  maskedPr = mask * pr
  mean_per_channel = tf.reduce_sum(maskedPr * gt, axis=[1, 2]) / tf.reduce_sum(maskedPr, axis=[1, 2])
  mean_per_image = tf.math.pow(tf.reduce_prod(mean_per_channel, axis=1), 1 / numberOfPoints)
  mean_per_batch = tf.math.reduce_mean(mean_per_channel)
  return 1 - mean_per_batch
