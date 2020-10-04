import numpy as np
import tensorflow as tf

from .constants import h, w
from ghost_scan.constants import numberOfPoints

pixelGrid = np.indices([h, w])
pixelGrid = np.transpose(pixelGrid, (1, 2, 0))
pixelGrid = pixelGrid / [h, w]
pixelGrid = np.expand_dims(pixelGrid, [0, 3])
pixelGrid = np.repeat(pixelGrid, numberOfPoints, axis=3)
pixelGrid = tf.constant(pixelGrid, dtype=tf.float32)
# truePositionsGrid is of shape (1, h, w, numberOfPoints, 2) and contains the (y, x) position of each pixel

def getY(deviatedCoords):
  'Returns, for each pixel, an array of len numberOfPoints. Each value is the gaussian of the distance between the pixel and the point'
  truePositionsGridsShape = tf.ones((1, h, w, numberOfPoints, 2), dtype=tf.float32)
  truePositionsGridMutiplier = tf.constant(deviatedCoords, dtype=tf.float32)
  truePositionsGrid = truePositionsGridsShape * truePositionsGridMutiplier

  squareDistances = tf.math.reduce_sum((pixelGrid - truePositionsGrid) ** 2, axis=-1)
  distances = tf.math.sqrt(squareDistances)
  Y = - tf.math.log(distances + 1e-7)
  return Y
