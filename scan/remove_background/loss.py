import tensorflow as tf

def loss(gt, pr):
  mask0 = tf.cast(gt == 0, dtype=pr.dtype)
  count0 = tf.math.reduce_sum(mask0)
  bce0 = - mask0 * tf.math.log(1 - pr + 1e-7)
  bce0 = tf.math.reduce_sum(bce0)

  mask1 = tf.cast(gt == 1, dtype=pr.dtype)
  count1 = tf.math.reduce_sum(mask1)
  bce1 = - mask1 * tf.math.log(pr + 1e-7)
  bce1 = tf.math.reduce_sum(bce1)

  loss = (bce0 / count0 + bce1 / count1) / 2
  return loss
