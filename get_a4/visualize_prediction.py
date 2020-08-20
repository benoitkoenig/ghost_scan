import matplotlib.pyplot as plt
import numpy as np
import sys
import tensorflow as tf

from ghost_scan.get_data import getPositions
from .data_generator import getXY
from .model import getModel

filename = sys.argv[1]

positions = getPositions(filename)
X, Y = getXY(filename, positions)
model = getModel(weights='./weights/get_a4')
pred = model.predict(X, steps=1)

print('Loss: %s' % tf.keras.losses.MeanSquaredError()(Y, pred).numpy())
print('Loss without the model: %s' % tf.keras.losses.MeanSquaredError()(Y, X[0, :, :, 16:19]).numpy())

fig, ax = plt.subplots(1, 3, figsize=(50, 50))
ax[0].imshow(X.numpy()[0, :, :, 16:20])
ax[1].imshow(np.clip(pred[0], 0, 1))
ax[2].imshow(Y.numpy()[0])
plt.show()
