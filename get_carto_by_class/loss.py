import tensorflow as tf

from ghost_scan.constants import numberOfPoints
from .constants import h, w

def getGtForHighestPrediction(gt, pr):
  flattenPixelPreds = tf.reshape(pr, (-1, numberOfPoints))
  flattenPixelsGt = tf.reshape(gt, (-1, numberOfPoints))

  indexOfEachHighestPrediction = tf.math.argmax(flattenPixelPreds, 0) # 1D tensor of len numberOfPoints
  allGtChannelsOfEachHighestPrediction = tf.gather(flattenPixelsGt, indexOfEachHighestPrediction)
  gtForHighestPrediction = tf.linalg.diag_part(allGtChannelsOfEachHighestPrediction)
  return gtForHighestPrediction

def loss(gt, pr):
  mask = tf.cast(gt != 0, dtype=pr.dtype)
  gtForHighestPrediction = getGtForHighestPrediction(gt, mask * pr) # shape=(numberOfPoints)
  adjustedGt = tf.stop_gradient(gt - gtForHighestPrediction)
  loss = mask * adjustedGt * (1 - pr) ** 2
  return loss
