import tensorflow as tf

from ghost_scan.constants import h, w, coords, numberOfPoints, dirpath
from ghost_scan.scan.remove_background.model import getModel

model = getModel(weights='%s/scan/models/weights/remove_background/weights' % dirpath)

def preprocessX(inputX):
  removeBackgroundPreds = model.predict(inputX, steps=1)
  removeBackgroundPreds = tf.convert_to_tensor(removeBackgroundPreds)
  outputX = tf.concat([inputX, removeBackgroundPreds], axis=-1)
  return outputX
