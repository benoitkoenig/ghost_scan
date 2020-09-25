import tensorflow as tf

from ghost_scan.constants import numberOfPoints

def loss(gt, pr):
  trueDeviations = tf.reshape(gt, (-1, numberOfPoints, 2))
  predDeviations = (tf.reshape(pr, (-1, numberOfPoints, 2)) - 0.5) * 0.1

  baseMse = tf.math.reduce_sum(trueDeviations ** 2, axis=-1)
  mse = tf.math.reduce_sum((trueDeviations - predDeviations) ** 2, axis=-1)
  loss = tf.reduce_mean((mse + 1e-4) / (baseMse + 1e-4))
  return loss
