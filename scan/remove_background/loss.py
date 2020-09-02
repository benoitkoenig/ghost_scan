import tensorflow as tf

def loss(gt, pr):
  gtdx, gtdy = tf.image.image_gradients(gt)
  prdx, prdy = tf.image.image_gradients(pr)
  mse = (gtdx - prdx) ** 2 + (gtdy - prdy) ** 2
  loss = tf.reduce_mean(mse)
  return loss
