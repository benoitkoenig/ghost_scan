import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from ghost_scan.constants import numberOfPoints
from .constants import h, w
from .data_generator import getSingleEntry
from .model import getModel
from .preprocess import postprocessPositions

filename = sys.argv[1]

model = getModel()
model.load_weights('./weights/get_cartography_by_points')
originalImage, originalPositions, X, Y, coords = getSingleEntry(filename)
rawPreds = model.predict(X, steps=1)
preds = postprocessPositions(rawPreds, coords)

print('Loss: %s' % tf.keras.losses.MeanSquaredError()(Y, rawPreds).numpy())

originalPositions = np.array(originalPositions)
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
