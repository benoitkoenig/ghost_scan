import numpy as np

from ghost_scan.constants import dirpath, numberOfPoints
from .model import getModel
from .postprocess import postprocess

class GetCartoByPoints:
  def __init__(self):
    self.model = getModel(weights='%s/scan/models/weights/detect_pose/weights' % dirpath)

  def predict(self, inputTensor, coords, outputShape):
    preds = self.model.predict(inputTensor, steps=1)
    positions = postprocess(preds[0], coords, outputShape[1:3])
    return positions
