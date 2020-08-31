import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from ghost_scan.constants import dirpath
from .get_data import getXY
from .constants import h, w
from .loss import loss
from .model import getModel

filename = sys.argv[1]

X, groundTruth = getXY([filename])
model = getModel('%s/scan/weights/get_carto_by_gradient/weights' % dirpath)
rawPreds = model.predict(X, steps=1)
preds = np.clip(rawPreds[0], 0, 1)

print('Loss: %s' % loss(groundTruth, rawPreds).numpy())

fig, axs = plt.subplots(2, 3, figsize=(50, 50))
axs[0, 0].imshow(X.numpy()[0])
axs[0, 1].imshow(preds)
axs[0, 2].imshow(groundTruth.numpy()[0])

predsRed = np.copy(preds)
predsRed[:, :, 1:] = 0

predsGreen = np.copy(preds)
predsGreen[:, :, 0] = 0
predsGreen[:, :, 2] = 0

predsBlue = np.copy(preds)
predsBlue[:, :, :2] = 0

axs[1, 0].imshow(predsRed)
axs[1, 1].imshow(predsGreen)
axs[1, 2].imshow(predsBlue)
plt.show()
