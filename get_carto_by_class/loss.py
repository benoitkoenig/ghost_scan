import tensorflow as tf

def loss(gt, pr):
  # TODO: a mean squared error is a very unsatisfactory loss
  return tf.keras.losses.MeanSquaredError()(gt, pr)
