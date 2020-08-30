import tensorflow as tf

def loss(gt, pr):
  mask = tf.cast(gt != 0, dtype=pr.dtype)
  maskedPr = mask * pr
  averages = tf.reduce_sum(maskedPr * gt, axis=[1, 2, 3]) / tf.reduce_sum(maskedPr, axis=[1, 2, 3])
  return 1 - tf.reduce_mean(averages)
