import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import sys
import tensorflow as tf

from ghost_scan.constants import coords, dirpath
from .constants import h, w
from .get_data import getSingleXY
from .loss import loss
from .model import getModel

coordsNp = np.array(coords)

filename = sys.argv[1]

X, Y, truePositions, rawX = getSingleXY(filename)
X = tf.constant([X], dtype=tf.float32)
Y = tf.constant([Y], dtype=tf.float32)
model = getModel(weights='%s/scan/models/weights/finetune_positions/weights' % dirpath)
preds = model.predict(X, steps=1)

print('Loss: %s' % loss(Y, tf.convert_to_tensor(preds)).numpy())

inputCoords = np.clip(coordsNp - np.reshape(Y.numpy(), (-1, 2)), 0, 1)
predsCoords = coordsNp - np.reshape((Y - preds).numpy(), (-1, 2))
inputPositions = griddata(coordsNp, truePositions, inputCoords, method='cubic')
predsPositions = griddata(coordsNp, truePositions, np.clip(predsCoords, 0, 1), method='cubic')

fig, axs = plt.subplots(1, 2, figsize=(50, 50))
axs[0].imshow(X.numpy()[0])
axs[0].plot((inputCoords * w)[:, 1], (inputCoords * h)[:, 0], marker='x')
axs[0].plot((predsCoords * w)[:, 1], (predsCoords * h)[:, 0], marker='o')
axs[1].imshow(rawX.numpy())
axs[1].plot(inputPositions[:, 1], inputPositions[:, 0], marker='x')
axs[1].plot(predsPositions[:, 1], predsPositions[:, 0], marker='o')
plt.show()
