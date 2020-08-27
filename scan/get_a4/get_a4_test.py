import numpy as np
import unittest

from .get_a4 import getOrigin

class TestStringMethods(unittest.TestCase):
  def test_getorigin(self):
    positions = np.array([[1, 1], [2, 5], [6, 3], [7, 8]])
    [originX, originY] = getOrigin(positions, 10, 10)
    self.assertEqual(originX[0, 0], 1)
    self.assertEqual(originX[9, 0], 6)
    self.assertEqual(originX[0, 9], 2)
    # self.assertEqual(originX[9, 9], 7)

    print(originX)
    print(originY)

if __name__ == '__main__':
    unittest.main()
