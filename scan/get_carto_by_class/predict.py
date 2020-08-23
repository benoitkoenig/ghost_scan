import numpy as np

from ghost_scan.scan.preprocess import resize
from .constants import h, w
from .model import getModel
from .postprocess import postprocess

def predict(inputTensor):
  X, coordsData = resize(inputTensor, h, w)
  mask = (X[:, :, :, 3] == 1).numpy()
  mask = np.stack([mask, mask, mask, mask], axis=-1)
  model = getModel(weights='./scan/weights/get_carto_by_class/weights')
  preds = model.predict(X, steps=1)
  maskedPreds = mask * preds
  positions = postprocess(maskedPreds, coordsData, inputTensor.shape[1:3])
  return positions
