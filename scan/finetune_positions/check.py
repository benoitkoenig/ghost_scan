import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import sys
import tensorflow as tf

from ghost_scan.constants import coords, dirpath
from ghost_scan.scan.get_a4.get_a4 import getA4
from .constants import h, w
from .deviations import getDeviationsFromGradients
from .get_data import getSingleXY
from .model import getModel

coordsNp = np.array(coords)

filename = sys.argv[1]

X, Y, rawX, deviatedCoords = getSingleXY(filename)
X = tf.convert_to_tensor([X], dtype=tf.float32)
Y = tf.convert_to_tensor([Y], dtype=tf.float32)
model = getModel(weights='%s/scan/models/weights/finetune_positions/weights' % dirpath)
preds = model.predict(X, steps=1)

coordsPredicted = coordsNp + 0.1 * getDeviationsFromGradients(2 * preds - 1)
originalCoordsInDeviatedPicture = 2 * coordsNp - deviatedCoords
coordsPredictedInOriginalPicture = deviatedCoords + 0.1 * getDeviationsFromGradients(2 * preds - 1)

fig, axs = plt.subplots(1, 2, figsize=(50, 50))

axs[0].set_title('Original Picture')
axs[0].imshow(rawX.numpy())
axs[0].plot(w * coordsNp[:, 1], h * coordsNp[:, 0], marker='x', label='Original coords')
axs[0].plot(w * deviatedCoords[:, 1], h * deviatedCoords[:, 0], marker='o', label='Deviated coords')
axs[0].plot(w * coordsPredictedInOriginalPicture[:, 1], h * coordsPredictedInOriginalPicture[:, 0], marker='^', label='Coords Predicted')
axs[0].legend()

axs[1].set_title('Input X')
axs[1].imshow(X.numpy()[0])
axs[1].plot(w * originalCoordsInDeviatedPicture[:, 1], h * originalCoordsInDeviatedPicture[:, 0], marker='x', label='Original coords')
axs[1].plot(w * coordsNp[:, 1], h * coordsNp[:, 0], marker='o', label='Deviated coords')
axs[1].plot(w * coordsPredicted[:, 1], h * coordsPredicted[:, 0], marker='^', label='Coords Predicted')
axs[1].legend()

plt.show()
