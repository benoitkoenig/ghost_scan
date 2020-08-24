import tensorflow as tf

def loss(gt, pr):
  mask0 = tf.cast(gt == 0, dtype=pr.dtype)
  mask1 = tf.cast(gt == 1, dtype=pr.dtype)

  num = mask1 * pr
  denom = num + 0.5 * mask0 * pr + 0.5 * mask1 * (1 - pr)
  loss = 1 - tf.math.reduce_sum(num) / tf.math.reduce_sum(denom)
  return loss
