import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from .get_data import getFullData
from .constants import h, w
from .loss import loss
from .metrics import meanSquareError
from .model import getModel
from .postprocess import postprocess

filename = sys.argv[1]

X, groundTruth, rawX, coords = getFullData(filename)
model = getModel('./scan/weights/get_carto_by_class/weights')
preds = model.predict(X, steps=1)
mask = (X.numpy()[:, :, :, 3] == 1)
maskedPreds = np.stack([mask, mask, mask, mask], axis=-1) * preds
positions = postprocess(maskedPreds, coords, rawX.shape[1:3])

print('Loss: %s' % tf.reduce_mean(loss(groundTruth, preds)).numpy())
print('MeanSquareError: %s' % meanSquareError(groundTruth, preds).numpy())

fig, axs = plt.subplots(2, 3, figsize=(50, 50))
axs[0, 0].imshow(rawX.numpy()[0])
axs[0, 0].plot(positions[:, 1], positions[:, 0], marker='x')
axs[1, 0].imshow(groundTruth.numpy()[0, :, :])
axs[0, 1].imshow(maskedPreds[0, :, :, 0])
axs[1, 1].imshow(maskedPreds[0, :, :, 1])
axs[0, 2].imshow(maskedPreds[0, :, :, 2])
axs[1, 2].imshow(maskedPreds[0, :, :, 3])
plt.show()
