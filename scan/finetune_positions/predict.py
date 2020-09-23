import numpy as np
from scipy.interpolate import griddata

from ghost_scan.constants import coords, dirpath
from ghost_scan.scan.get_a4.get_a4 import getA4

from .constants import h, w
from .model import getModel

class FinetunePositions:
  def __init__(self):
    self.model = getModel(weights='%s/scan/weights/finetune_positions/weights' % dirpath)

  def predict(self, inputImage, inputPositions):
    X = getA4(inputImage, inputPositions, h, w)
    preds = self.model.predict(np.array([X]), steps=1)
    preds = np.reshape(preds[0], (-1, 2))
    newCoords = np.clip(coords - preds, 0, 1)
    outputPositions = griddata(coords, inputPositions, newCoords, method='cubic')
    return outputPositions
