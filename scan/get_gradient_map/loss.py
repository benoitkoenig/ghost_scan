import tensorflow as tf

def gradientLoss(gt, pr):
  gtdx, gtdy = tf.image.image_gradients(gt)
  prdx, prdy = tf.image.image_gradients(pr)
  mse = (gtdx - prdx) ** 2 + (gtdy - prdy) ** 2
  loss = tf.math.reduce_mean(mse)
  return loss

def segmentationLoss(gt, pr):
  mse = tf.math.reduce_mean((gt - pr) ** 2)
  loss = tf.math.reduce_mean(mse)
  return loss

def loss(gt, pr):
  loss = (gradientLoss(gt, pr) + segmentationLoss(gt, pr)) / 2
  return loss
