import tensorflow as tf

from ghost_scan.constants import numberOfPoints

def loss(gt, pr):
  prEpsilon = pr + 1e-5 # 1e-5 is here to prevent the lowest pr to converge to 0, forcing the highest pr to converge to 1 instead. 1e-5 times all the mask's pixels is close to 1
  mean_per_channel = tf.reduce_sum(prEpsilon * gt, axis=[1, 2]) / (tf.reduce_sum(prEpsilon, axis=[1, 2]) + 1e-7) # 1e-7 is useful when the document is fully out of the picture, which can occasionnaly happen
  mean_per_image = tf.math.pow(tf.reduce_prod(mean_per_channel, axis=1), 1 / numberOfPoints)
  mean_per_batch = tf.math.reduce_mean(mean_per_channel)
  return - mean_per_batch
