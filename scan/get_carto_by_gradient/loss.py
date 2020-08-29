import tensorflow as tf

def loss(gt, pr):
  mask = tf.cast(gt[:, :, :, 0] == 1, gt.dtype)
  mask = tf.stack([mask, mask, mask], axis=-1)
  loss = tf.math.reduce_sum((mask * (gt - pr)) ** 2) / tf.math.reduce_sum(mask)
  return loss
