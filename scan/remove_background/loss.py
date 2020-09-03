import tensorflow as tf

def loss(gt, pr):
  gtdx, gtdy = tf.image.image_gradients(gt)
  prdx, prdy = tf.image.image_gradients(pr)
  mask = tf.cast((gtdx != 0) | (gtdy != 0), dtype=pr.dtype)
  mse = (gtdx - prdx) ** 2 + (gtdy - prdy) ** 2
  loss = 0.5 * (tf.reduce_mean(mask * mse) + tf.reduce_mean((1 - mask) * mse))
  return loss
