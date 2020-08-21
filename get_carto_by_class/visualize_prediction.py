import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from .data_generator import getXY
from .constants import h, w
from .loss import loss
from .metrics import meanSquareError
from .model import getModel

filename = sys.argv[1]

X, groundTruth = getXY(filename)
model = getModel('weights/get_carto_by_class')
preds = model.predict(X, steps=1)

print('Loss: %s' % loss(groundTruth, preds).numpy())
print('MeanSquareError: %s' % meanSquareError(groundTruth, preds).numpy())

fig, axs = plt.subplots(1, 5, figsize=(50, 50))
axs[0].imshow(X.numpy()[0])
axs[1].imshow(preds[0, :, :, 0])
axs[2].imshow(preds[0, :, :, 1])
axs[3].imshow(preds[0, :, :, 2])
axs[4].imshow(preds[0, :, :, 3])
plt.show()
