import tensorflow as tf

from .model import getModel
from .preprocess import preprocess, postprocessPositions

def predict(inputTensor):
  X, coordsData = preprocess(inputTensor)
  model = getModel(weights='./scan/weights/get_carto_by_points/weights')
  preds = model.predict(X, steps=1)
  positions = postprocessPositions(preds, coordsData)
  return positions
