import tensorflow as tf

from ghost_scan.constants import numberOfPoints

def getGtForHighestPrediction(gt, pr):
  flattenPixelPreds = tf.reshape(pr, (-1, numberOfPoints))
  flattenPixelsGt = tf.reshape(gt, (-1, numberOfPoints))

  indexOfEachHighestPrediction = tf.math.argmax(flattenPixelPreds, 0) # 1D tensor of len numberOfPoints
  allGtChannelsOfEachHighestPrediction = tf.gather(flattenPixelsGt, indexOfEachHighestPrediction)
  gtForHighestPrediction = tf.linalg.diag_part(allGtChannelsOfEachHighestPrediction)
  return gtForHighestPrediction

def meanSquareError(gt, pr):
  # Note: The two first parts are copy/paste from loss.py. I keep them seperated for now

  # First, get the mask. It is where all gaussian distances are zeros
  mask = tf.cast(gt != 0, dtype=pr.dtype)

  # Then, get the gt of all best predictions
  gtForHighestPrediction = getGtForHighestPrediction(gt, mask * pr)
  assert(gtForHighestPrediction.shape == (numberOfPoints))
  
  # Finally, get the meanSquareDistance
  squareDistances = - tf.math.log(gtForHighestPrediction)
  meanSquareDistance = tf.math.reduce_mean(squareDistances)

  return meanSquareDistance
