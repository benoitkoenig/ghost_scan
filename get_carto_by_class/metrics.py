import tensorflow as tf

from ghost_scan.constants import numberOfPoints

def meanSquareError(gt, pr):
  # Note: The two first parts are copy/paste from loss.py. I keep them seperated for now

  # First, get the mask. It is where all gaussian distances are zeros
  mask = tf.cast(gt != 0, dtype=pr.dtype)
  maskedPreds = mask * pr

  # Then, get the gt of all best predictions
  flattenPixelPreds = tf.reshape(maskedPreds, (-1, numberOfPoints))
  flattenPixelsGt = tf.reshape(gt, (-1, numberOfPoints))
  bestPredPerPoint = tf.math.argmax(flattenPixelPreds, 0) # 1D tensor of len numberOfPoints
  gtOfBestPrediction = tf.linalg.diag_part(tf.gather(flattenPixelsGt, bestPredPerPoint))
  
  # Finally, get the meanSquareDistance
  squareDistances = - tf.math.log(gtOfBestPrediction)
  meanSquareDistance = tf.math.reduce_mean(squareDistances)

  return meanSquareDistance
