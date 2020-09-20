import tensorflow as tf

from ghost_scan.constants import numberOfPoints

def loss(gt, pr):
  mean_per_channel = tf.reduce_sum(pr * gt, axis=[1, 2]) / (tf.reduce_sum(pr, axis=[1, 2]) + 1e-7) # 1e-7 is useful when the document is fully out of the picture, which can occasionnaly happen
  mean_per_batch = tf.math.reduce_mean(mean_per_channel)
  return - mean_per_batch
