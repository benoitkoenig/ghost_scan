import tensorflow as tf

from ghost_scan.constants import numberOfPoints

def getGtForHighestPrediction(gt, pr):
  flattenPixelPreds = tf.reshape(pr, (-1, numberOfPoints))
  flattenPixelsGt = tf.reshape(gt, (-1, numberOfPoints))

  indexOfEachHighestPrediction = tf.math.argmax(flattenPixelPreds, axis=0) # 1D tensor of len numberOfPoints
  allGtChannelsOfEachHighestPrediction = tf.gather(flattenPixelsGt, indexOfEachHighestPrediction)
  gtForHighestPrediction = tf.linalg.diag_part(allGtChannelsOfEachHighestPrediction)
  return gtForHighestPrediction

def bestPredDistance(gt, pr):
  # First, get the mask. It is where all gt are non-zero
  mask = tf.cast(gt != 0, dtype=pr.dtype)

  # Then, get the gt of all best predictions
  gtForHighestPrediction = getGtForHighestPrediction(gt, mask * pr)
  assert(gtForHighestPrediction.shape == (numberOfPoints))

  # Finally, get the meanDistance
  distances = - tf.math.log(gtForHighestPrediction)
  meanDistance = tf.math.reduce_mean(distances)

  return meanDistance
