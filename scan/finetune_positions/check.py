import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import sys
import tensorflow as tf

from ghost_scan.constants import coords, dirpath
from ghost_scan.scan.get_a4.get_a4 import getA4
from .constants import h, w
from .get_data import getSingleXY
from .model import getModel

coordsNp = np.array(coords)

filename = sys.argv[1]

X, Y, rawX, deviatedPositions, truePositions, deviatedCoords = getSingleXY(filename)
X = tf.convert_to_tensor([X], dtype=tf.float32)
Y = tf.convert_to_tensor([Y], dtype=tf.float32)
model = getModel(weights='%s/scan/models/weights/finetune_positions/weights' % dirpath)
preds = model.predict(X, steps=1)

truePicture = getA4(rawX.numpy(), truePositions, h, w)
coordsPlusY = coordsNp - (np.reshape(Y, (-1, 2)) - 0.5) * 0.1
coordsPlusPreds = coordsNp - (np.reshape(preds, (-1, 2)) - 0.5) * 0.1

fig, axs = plt.subplots(1, 3, figsize=(50, 50))

axs[0].set_title('Scanned document from true positions')
axs[0].imshow(truePicture)
axs[0].plot(w * coordsNp[:, 1], h * coordsNp[:, 0], marker='^', label='Ground truth')
axs[0].plot(w * deviatedCoords[:, 1], h * deviatedCoords[:, 0], marker='o', label='Given coords')
axs[0].legend()

axs[1].set_title('Printed document picture')
axs[1].imshow(rawX.numpy())
axs[1].plot(truePositions[:, 1], truePositions[:, 0], marker='^', label='Ground truth')
axs[1].plot(deviatedPositions[:, 1], deviatedPositions[:, 0], marker='o', label='Given positions')
axs[1].legend()

axs[2].set_title('Input picture')
axs[2].imshow(X.numpy()[0])
axs[2].plot(w * coordsPlusY[:, 1], h * coordsPlusY[:, 0], marker='^', label='Ground truth (Coords + Y)')
axs[2].plot(w * coordsNp[:, 1], h * coordsNp[:, 0], marker='o', label='Coords')
axs[2].plot(w * coordsPlusPreds[:, 1], h * coordsPlusPreds[:, 0], marker='x', label='Coords + Preds')
axs[2].legend()

plt.show()
