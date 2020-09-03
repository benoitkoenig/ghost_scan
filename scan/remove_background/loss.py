import tensorflow as tf

def loss(gt, pr):
  gtdx, gtdy = tf.image.image_gradients(gt)
  prdx, prdy = tf.image.image_gradients(pr)
  mask = tf.cast((gtdx != 0) | (gtdy != 0), dtype=pr.dtype)
  mse = (gtdx - prdx) ** 2 + (gtdy - prdy) ** 2
  loss1 = tf.math.reduce_sum(mask * mse) / tf.math.reduce_sum(mask)
  loss0 = tf.math.reduce_sum((1 - mask) * mse) / tf.math.reduce_sum(1 - mask)
  loss = (loss0 + loss1) / 2
  return loss
