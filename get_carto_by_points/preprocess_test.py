import numpy as np
import tensorflow as tf
import unittest

from .constants import h, w
from .preprocess import getRelevantAreaCoords, preprocessForTraining

class TestPreprocess(unittest.TestCase):
  def test_getRelevantAreaCoords(self):
    zero = [0, 0, 0, 0]
    ones = [1, 1, 1, 1]
    inputData = np.array([[
      [zero, zero, zero, zero, zero],
      [zero, zero, zero, zero, zero],
      [zero, zero, ones, zero, zero],
      [zero, ones, ones, zero, zero],
      [zero, zero, zero, zero, zero],
    ]])
    (y1, x1, y2, x2) = getRelevantAreaCoords(inputData)
    self.assertEqual((y1, x1, y2, x2), (2, 1, 3, 2))

  def test_preprocessForTraining(self):
    zero = [0, 0, 0, 0]
    ones = [1, 1, 1, 1]
    inputTensor = tf.constant([[
      [zero, zero, zero, zero, zero],
      [zero, zero, zero, zero, zero],
      [zero, zero, ones, zero, zero],
      [zero, ones, ones, zero, zero],
      [zero, zero, zero, zero, zero],
    ]])
    X, Y = preprocessForTraining(inputTensor, [[2, 1], [3, 2]])
    self.assertEqual(X.shape, (1, h, w, 4))
    Xnumpy = X.numpy()
    self.assertEqual(Xnumpy[0, 0, 0, 3], 0)
    self.assertEqual(Xnumpy[0, 255, 0, 3], 1)
    self.assertEqual(Xnumpy[0, 0, 255, 3], 1)
    self.assertEqual(Xnumpy[0, 255, 255, 3], 1)
    self.assertEqual(Y.tolist(), [[0, 0], [h - 1, w - 1]])

if __name__ == '__main__':
  unittest.main()
