import numpy as np
import tensorflow as tf
import unittest

from .constants import h, w
from ghost_scan.constants import numberOfPoints
from .loss import getGtForHighestPrediction

class TestPreprocess(unittest.TestCase):
  def test_getGtForHighestPrediction(self):
    pr = np.zeros((1, h, w, numberOfPoints)) + 0.2
    pr[0, 0, 0, :] = 0.6
    pr[0, 1, 0, 0] = 0.7
    pr = tf.convert_to_tensor(pr)
    gt = np.zeros((1, h, w, numberOfPoints))
    gt[0, 0, 0, :] = 0.8
    gt[0, 1, 0, 0] = 0.9
    gt = tf.convert_to_tensor(gt)
    output = getGtForHighestPrediction(gt, pr)
    self.assertEqual(output.numpy().tolist(), [0.9] + [0.8] * (numberOfPoints - 1))

if __name__ == '__main__':
  unittest.main()
