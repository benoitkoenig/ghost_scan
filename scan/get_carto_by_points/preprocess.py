import tensorflow as tf

from ghost_scan.constants import h, w, coords, numberOfPoints, dirpath
from ghost_scan.scan.remove_background.model import getModel

model = getModel(weights='%s/scan/weights/remove_background/weights' % dirpath)

def preprocessX(inputX):
  outputX = model.predict(inputX, steps=1)
  outputX = tf.convert_to_tensor(outputX)
  return outputX

pointsGridsShape = tf.ones((1, h, w, numberOfPoints, 2), dtype=tf.float32)
pointsGridMutiplier = tf.convert_to_tensor(coords, dtype = tf.float32)
pointsGrid = pointsGridsShape * pointsGridMutiplier
# pointsGrid is of shape (1, h, w, numberOfPoints, 2) and contains the array coords on each pixel

def preprocessY(inputY):
  'Returns, for each pixel, an array of len numberOfPoints. Each value is the gaussian of the distance between the pixel and the point'
  mask = inputY[:, :, :, 0] == 1
  mask = tf.reshape(tf.repeat(mask, numberOfPoints, axis=-1), (-1, h, w, numberOfPoints))

  stackedChannels = tf.reshape(inputY[:, :, :, 1:3], (-1, h, w, 1, 2))
  stackedChannels = tf.repeat(stackedChannels, numberOfPoints, axis=-2)

  squareDistances = tf.math.reduce_sum((stackedChannels - pointsGrid) ** 2, axis=-1)
  distances = tf.math.sqrt(squareDistances)

  Y = - tf.math.log(distances + 1e-7)
  Y = tf.cast(mask, dtype=Y.dtype) * Y
  return Y
