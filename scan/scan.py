import numpy as np

from ghost_scan.scan.remove_background.predict import RemoveBackground
from ghost_scan.scan.get_carto_by_points.predict import GetCartoByPoints
from ghost_scan.scan.get_a4.get_a4 import getA4

removeBackground = RemoveBackground()
getCartoByPoints = GetCartoByPoints()

def scan(inputData):
  inputImage = np.array(inputData)
  imageWithoutBackground = removeBackground.predict(inputImage)
  positions = getCartoByPoints.predict(imageWithoutBackground)
  documentA4 = getA4(inputImage[0], positions)
  return documentA4
