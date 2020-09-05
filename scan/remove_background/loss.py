import tensorflow as tf

def gradientLoss(gt, pr):
  gtdx, gtdy = tf.image.image_gradients(gt)
  prdx, prdy = tf.image.image_gradients(pr)
  mask = tf.cast((gtdx != 0) | (gtdy != 0), dtype=pr.dtype)
  mse = (gtdx - prdx) ** 2 + (gtdy - prdy) ** 2

  gradientLoss1 = tf.math.reduce_sum(mask * mse) / tf.math.reduce_sum(mask)
  gradientLoss0 = tf.math.reduce_sum((1 - mask) * mse) / tf.math.reduce_sum(1 - mask)
  gradientLoss = (gradientLoss0 + gradientLoss1) / 2

  return gradientLoss

def segmentationLoss(gt, pr):
  segmentationLoss = tf.math.reduce_mean((gt - pr) ** 2)
  return segmentationLoss

def loss(gt, pr):
  loss = (gradientLoss(gt, pr) + segmentationLoss(gt, pr)) / 2
  return loss
