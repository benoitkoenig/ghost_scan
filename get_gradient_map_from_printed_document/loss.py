import tensorflow as tf

def removeFadingBordersFromGroundTruth(gt):
  [tensorRed, tensorGreen, tensorBlue] = tf.split(gt, 3, axis=3)
  tensorRed = tf.cast(tensorRed == 1, gt.dtype)
  tensorGreen = tensorRed * tensorGreen
  tensorBlue = tensorRed * tensorBlue
  newGt = tf.concat([tensorRed, tensorGreen, tensorBlue], axis=3)
  return newGt

def capPredToOneWhenRelevant(gt, pr):
  "When ground truth is 1, predicting more than 1 is a valid answer"
  capToOne = tf.cast((gt == 1) & (pr > 1), dtype=pr.dtype)
  newPr = capToOne + (1 - capToOne) * pr
  return newPr

def capPredToZeroWhenRelevant(gt, pr):
  "When ground truth is 0, predicting less than 0 is a valid answer"
  capToZero = tf.cast((gt == 0) & (pr < 0), dtype=pr.dtype)
  newPr = (1 - capToZero) * pr
  return newPr

def loss(gt, pr):
  newGt = removeFadingBordersFromGroundTruth(gt)
  newPr = capPredToOneWhenRelevant(gt, pr)
  newPr = capPredToZeroWhenRelevant(gt, newPr)

  return tf.math.reduce_mean((newGt - newPr) ** 2)
