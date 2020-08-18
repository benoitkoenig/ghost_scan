import tensorflow as tf

def loss(gt, pr):
  [tensorRed, _, _] = tf.split(gt, 3, axis=3)
  tensorRelevant = tf.cast(tensorRed == 1, gt.dtype)
  return tf.math.reduce_sum((tensorRelevant * (gt - pr)) ** 2) / tf.math.reduce_sum(tensorRelevant)
