import numpy as np

from ghost_scan.scan.remove_background.predict import predict as predictImageWithoutBackground
from ghost_scan.scan.get_carto_by_points.predict import predict as predictPositions
from ghost_scan.scan.get_a4.get_a4 import getA4

def scan(inputData):
  inputImage = np.array(inputData)
  imageWithoutBackground = predictImageWithoutBackground(inputImage)
  positions = predictPositions(imageWithoutBackground)
  documentA4 = getA4(inputImage[0], positions)
  return documentA4
