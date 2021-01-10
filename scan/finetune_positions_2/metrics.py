import tensorflow as tf

def relativeMse(gt, pr):
  trueY = tf.reshape(gt - 0.5, (-1, 2))
  squareTrueY = tf.math.square(trueY)
  trueMsePerPoint = tf.math.reduce_sum(squareTrueY, axis=-1)

  predictionError = tf.reshape(gt - pr, (-1, 2))
  squarePredictionError = tf.math.square(predictionError)
  predictionMsePerPoint = tf.math.reduce_sum(squarePredictionError, axis=-1)

  relativeMsePerPoint = predictionMsePerPoint - trueMsePerPoint
  finalRelativeMse = tf.math.reduce_mean(relativeMsePerPoint)

  return finalRelativeMse
