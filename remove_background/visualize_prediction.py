import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from .constants import h, w
from .data_generator import getXY
from .model import getModel

filename = sys.argv[1]

X, groundTruth = getXY(filename)
model = getModel(weights='weights/remove_background')
prediction = model.predict(X, steps=1)

fig, axs = plt.subplots(1, 3, figsize=(50, 50))
axs[0].imshow(X.numpy()[0])
axs[1].imshow(np.reshape(groundTruth.numpy(), (h, w)))
axs[2].imshow(np.reshape(prediction, (h, w)))
plt.show()
