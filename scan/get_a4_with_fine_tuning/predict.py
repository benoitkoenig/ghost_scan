from .model import getModel
from .preprocess import preprocess

def predict(inputTensor, positions):
  X = preprocess(inputTensor, positions)
  model = getModel(weights='./scan/weights/get_a4/weights')
  pred = model.predict(X, steps=1)
  return pred
