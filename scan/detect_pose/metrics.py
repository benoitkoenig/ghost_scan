import tensorflow as tf

from ghost_scan.constants import numberOfPoints, h, w

def getGtForHighestPrediction(gt, pr):
  flattenPixelPreds = tf.reshape(pr, (-1, h * w, numberOfPoints))
  flattenPixelsGt = tf.reshape(gt, (-1, h * w, numberOfPoints))

  indexOfEachHighestPrediction = tf.math.argmax(flattenPixelPreds, axis=1)
  allGtChannelsOfEachHighestPrediction = tf.gather(flattenPixelsGt, indexOfEachHighestPrediction, axis=1)
  gtForHighestPrediction = tf.linalg.diag_part(allGtChannelsOfEachHighestPrediction)
  gtForHighestPrediction = tf.transpose(gtForHighestPrediction, [2, 0, 1])
  gtForHighestPrediction = tf.linalg.diag_part(gtForHighestPrediction)
  gtForHighestPrediction = tf.transpose(gtForHighestPrediction, [1, 0])
  return gtForHighestPrediction

def getHighestGt(gt):
  highestGt = tf.math.reduce_max(gt, axis=[1, 2])
  return highestGt

def bestPredDistance(gt, pr):
  highestGt = getHighestGt(gt)
  gtForHighestPrediction = getGtForHighestPrediction(gt, pr)
  # highestGt.shape == gtForHighestPrediction.shape == (batchSize, numberOfPoints)

  bestPredDistances = tf.math.exp(-gtForHighestPrediction)
  optimalDistances = tf.math.exp(-highestGt)

  distancesFromOptimal = bestPredDistances - optimalDistances
  meanDistanceFromOptimal = tf.math.reduce_mean(distancesFromOptimal)

  return meanDistanceFromOptimal
