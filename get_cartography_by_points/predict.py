import tensorflow as tf

from .model import getModel
from .preprocess import preprocess, postprocessPositions

def predict(inputTensor):
  X, coordsData = preprocess(inputTensor)
  model = getModel(weights='weights/get_cartography_by_points')
  preds = model.predict(X, steps=1)
  positions = postprocessPositions(preds, coordsData)
  return positions
