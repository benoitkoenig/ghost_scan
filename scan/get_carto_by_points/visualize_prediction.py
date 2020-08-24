import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from ghost_scan.constants import numberOfPoints
from ghost_scan.scan.get_data import getPositions
from .constants import h, w
from .get_data import getXY
from .model import getModel
from .preprocess import postprocessPositions

filename = sys.argv[1]

positions = getPositions(filename)
X, Y, originalImage, coords = getXY(filename, positions)
model = getModel(weights='./scan/weights/get_carto_by_points/weights')
rawPreds = model.predict(X, steps=1)
preds = postprocessPositions(rawPreds, coords)

print('Loss: %s' % tf.keras.losses.MeanSquaredError()(Y, rawPreds).numpy())

originalPositions = np.array(positions)
fig, ax = plt.subplots(1, 2, figsize=(50, 50))
ax[0].imshow(originalImage.numpy()[0])
ax[0].plot(originalPositions[:, 1], originalPositions[:, 0], marker='o')
ax[0].plot(preds[:, 1], preds[:, 0], marker='x')

Y = np.reshape(Y.numpy(), (numberOfPoints, 2))
rawPreds = np.reshape(rawPreds, (numberOfPoints, 2))
ax[1].imshow(X.numpy()[0])
ax[1].plot(Y[:, 1] * w, Y[:, 0] * h, marker='o')
ax[1].plot(rawPreds[:, 1] * w, rawPreds[:, 0] * h, marker='x')
plt.show()
