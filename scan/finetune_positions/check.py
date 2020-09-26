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

X, Y, rawX, deviatedPositions, truePositions = getSingleXY(filename)
X = tf.convert_to_tensor([X], dtype=tf.float32)
Y = tf.convert_to_tensor([Y], dtype=tf.float32)
model = getModel(weights='%s/scan/models/weights/finetune_positions/weights' % dirpath)
preds = model.predict(X, steps=1)

print('Loss: %s' % loss(Y, tf.convert_to_tensor(preds)).numpy())

coordsToPredict = coordsNp + np.reshape(Y, (-1, 2))
positionsToPredict = griddata(coordsNp, deviatedPositions, np.clip(coordsToPredict, 0, 1), method='cubic')

coordsPredicted = coordsNp + (np.reshape(preds, (-1, 2)) - 0.5) * 0.1
positionsPredicted = griddata(coordsNp, deviatedPositions, np.clip(coordsPredicted, 0, 1), method='cubic')

fig, axs = plt.subplots(1, 2, figsize=(50, 50))

axs[0].imshow(X.numpy()[0])
axs[0].plot((coordsToPredict * w)[:, 1], (coordsToPredict * h)[:, 0], marker='^', label='ground truth')
axs[0].plot((coordsNp * w)[:, 1], (coordsNp * h)[:, 0], marker='o', label='deviated coords')
axs[0].plot((coordsPredicted * w)[:, 1], (coordsPredicted * h)[:, 0], marker='x', label='preds')
axs[1].imshow(rawX.numpy())
axs[1].plot(truePositions[:, 1], truePositions[:, 0], marker='^', label='groundTruth')
axs[1].plot(positionsToPredict[:, 1], positionsToPredict[:, 0], marker='o', label='deviated positions')
axs[1].plot(positionsPredicted[:, 1], positionsPredicted[:, 0], marker='x', label='preds')

axs[0].legend()
plt.show()
