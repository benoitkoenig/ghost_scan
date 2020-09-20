import numpy as np

from ghost_scan.scan.remove_background.predict import RemoveBackground
from ghost_scan.scan.detect_pose.predict import GetCartoByPoints
from ghost_scan.scan.get_a4.get_a4 import getA4

removeBackground = RemoveBackground()
getCartoByPoints = GetCartoByPoints()

def scan(inputData):
  inputImage = np.array(inputData)
  removeBackgroundPreds, coords = removeBackground.predict(inputImage)
  positions = getCartoByPoints.predict(removeBackgroundPreds, coords, inputImage.shape)
  documentA4 = getA4(inputImage[0], positions)
  return documentA4
