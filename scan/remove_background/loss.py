import tensorflow as tf
import tensorflow_addons as tfa

epsilon = 1e-7

def loss(gt, pr):
  blurryGt = tfa.image.median_filter2d(gt, 9, padding='CONSTANT', constant_values=0)
  weights = 0.2 + (gt * (1 - blurryGt) + (1 - gt) * blurryGt) * 2
  bce = - (gt * tf.math.log(pr + epsilon) + (1 - gt) * tf.math.log(1 - pr + epsilon))
  loss = tf.reduce_mean(weights * bce)
  return loss
