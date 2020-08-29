import random
import tensorflow as tf
import unittest

from .preprocess import preprocessTrainingOnly

class TestStringMethods(unittest.TestCase):
  def test_preprocessTrainingOnly(self):
    inputX = tf.random.uniform((50, 8, 9, 3))
    X = preprocessTrainingOnly(inputX)
    self.assertEqual(inputX.shape, X.shape)
    for i in range(50):
      for j in range(3):
        self.assertEqual(
          X[i, random.randint(0, 7), random.randint(0, 8), j] == 0,
          X[i, random.randint(0, 7), random.randint(0, 8), j] == 0,
        )
    print(X)

if __name__ == '__main__':
    unittest.main()
