import numpy as np

from ghost_scan.scan.remove_background.predict import RemoveBackground
from ghost_scan.scan.detect_pose.predict import GetCartoByPoints
from ghost_scan.scan.finetune_positions.predict import FinetunePositions
from ghost_scan.scan.get_a4.get_a4 import getA4

removeBackground = RemoveBackground()
getCartoByPoints = GetCartoByPoints()
finetunePositions = FinetunePositions()

def scan(inputData):
  inputImage = np.array(inputData)
  removeBackgroundPreds, coords = removeBackground.predict(inputImage)
  positions = getCartoByPoints.predict(removeBackgroundPreds, coords, inputImage.shape)
  finetunedPositions = finetunePositions(inputImage, positions)
  documentA4 = getA4(inputImage[0], finetunedPositions)
  return documentA4
