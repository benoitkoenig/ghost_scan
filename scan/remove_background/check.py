import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from ghost_scan.constants import h, w, dirpath
from .get_data import getXY
from .loss import loss, segmentationLoss, gradientLoss
from .model import getModel

filename = sys.argv[1]

X, groundTruth = getXY([filename])
model = getModel(weights='%s/scan/weights/remove_background/weights' % dirpath)
preds = model.predict(X, steps=1)

print('Loss: %s' % loss(groundTruth, tf.convert_to_tensor(preds)).numpy())
print('Segmentation Loss: %s' % segmentationLoss(groundTruth, tf.convert_to_tensor(preds)).numpy())
print('Gradient Loss: %s' % gradientLoss(groundTruth, tf.convert_to_tensor(preds)).numpy())

fig, axs = plt.subplots(1, 3, figsize=(50, 50))
axs[0].imshow(X.numpy()[0])
axs[1].imshow(np.reshape(groundTruth.numpy(), (h, w)))
axs[2].imshow(np.reshape(preds, (h, w)))
plt.show()
