import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from .constants import h, w, numberOfPoints
from .data_generator import getSingleEntry
from .model import getModel

filename = sys.argv[1]

model = getModel()
model.load_weights('./weights/get_cartography_from_printed_document_without_background')
X, groundTruth = getSingleEntry(filename)
pred = model.predict(X, steps=1)
print('Loss: %s' % tf.keras.losses.MeanSquaredError()(groundTruth, pred).numpy())

groundTruthY = np.array([groundTruth[0][2*i] for i in range(numberOfPoints)]) * h
groundTruthX = np.array([groundTruth[0][2*i+1] for i in range(numberOfPoints)]) * w

predY = np.array([pred[0][2*i] for i in range(numberOfPoints)]) * h
predX = np.array([pred[0][2*i+1] for i in range(numberOfPoints)]) * w

fig, ax = plt.subplots(1, 1, figsize=(50, 50))
ax.imshow(X.numpy()[0])
ax.plot(groundTruthX, groundTruthY, marker='o')
ax.plot(predX, predY, marker='x')
plt.show()
