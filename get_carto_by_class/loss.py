import tensorflow as tf

from ghost_scan.constants import numberOfPoints

def loss(gt, pr):
  # gt and pr are both of shape (1, h, w, numberOfPoints)

  # First, get the mask. It is where all gaussian distances are zeros
  mask = tf.cast(gt != 0, dtype=pr.dtype)
  maskedPreds = mask * pr

  # Then, get the gt of all best predictions
  flattenPixelPreds = tf.reshape(maskedPreds, (-1, numberOfPoints))
  flattenPixelsGt = tf.reshape(gt, (-1, numberOfPoints))
  bestPredPerPoint = tf.math.argmax(flattenPixelPreds, 0) # 1D tensor of len numberOfPoints
  gtOfBestPrediction = tf.linalg.diag_part(tf.gather(flattenPixelsGt, bestPredPerPoint))

  # The adjusted ground truth is the gt minus the gt of the best prediction. So adjustedGT > 0 for points closer than the current best guess, < 0 otherwise
  adjustedGt = tf.stop_gradient(gt - gtOfBestPrediction)

  # The loss is the cross-entropy of the prediction times the adjusted ground truth. It will move up where adjustedGT > 0, and down where adjustedGt < 0
  loss = - mask * adjustedGt * tf.math.log(pr)
  loss = tf.math.reduce_sum(loss) / tf.math.reduce_sum(maskedPreds)

  return loss
