import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from ghost_scan.constants import dirpath, numberOfPoints
from .get_data import getFullData
from .loss import loss, prAsCoeffLoss, actualNearestPixelsMse, getTruePixelMask
from .metrics import bestPredDistance
from .model import getModel
from .postprocess import postprocess

filename = sys.argv[1]

X, groundTruth, rawX, coords = getFullData(filename)
truePixelMask = getTruePixelMask(groundTruth).numpy()
model = getModel('%s/scan/models/weights/detect_pose/weights' % dirpath)
preds = model.predict(X, steps=1)
positions = postprocess(preds[0], coords, rawX.shape[1:3])

print('Loss: %s' % loss(groundTruth, preds).numpy())
print('PrAsCoeff loss: %s' % prAsCoeffLoss(groundTruth, preds).numpy())
print('Actual Nearest Pixels Mse: %s' % actualNearestPixelsMse(groundTruth, preds).numpy())
print('Best pred distance: %s' % bestPredDistance(groundTruth, preds).numpy())

predsSingleChannel = np.clip(np.sum(preds[0], axis=-1), 0, 1)
predsSingleChannel = np.expand_dims(predsSingleChannel, axis=-1)
truePixelMaskSingleChannel = np.sum(truePixelMask[0], axis=-1)
truePixelMaskSingleChannel = np.expand_dims(truePixelMaskSingleChannel, axis=-1)
comparaison = np.concatenate([truePixelMaskSingleChannel, (truePixelMaskSingleChannel == 1) & (predsSingleChannel > .9), predsSingleChannel], axis=-1)

fig, axs = plt.subplots(2, 3, figsize=(50, 50))
axs[0, 0].imshow(rawX.numpy()[0, :, :])
axs[0, 0].plot(positions[:, 1], positions[:, 0], marker='x')
axs[1, 0].imshow(groundTruth.numpy()[0, :, :, 0])
axs[0, 1].imshow(preds[0, :, :, 0:3])
axs[1, 1].imshow(preds[0, :, :, 3:6])
axs[0, 2].imshow(preds[0, :, :, 6:9])
axs[1, 2].imshow(comparaison)
plt.show()
