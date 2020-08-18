import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from .data_generator import getTensorFromFilepathPng
from .constants import h, w
from .loss import loss
from .model import getModel

filename = sys.argv[1]

model = getModel('weights/get_cartography_by_gradient.h5')
X = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, h, w, keepAlphaChannel=True)
groundTruth = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename, h, w)
rawPrediction = model.predict(X, steps=1)

print('Loss: %s' % loss(groundTruth, rawPrediction).numpy())

prediction = np.clip(rawPrediction[0], 0, 1)

fig, axs = plt.subplots(2, 3, figsize=(50, 50))
axs[0, 0].imshow(X.numpy()[0])
axs[0, 1].imshow(prediction)
axs[0, 2].imshow(groundTruth.numpy()[0])

predictionRed = np.copy(prediction)
predictionRed[:, :, 1] = 0
predictionRed[:, :, 2] = 0

predictionGreen = np.copy(prediction)
predictionGreen[:, :, 0] = 0
predictionGreen[:, :, 2] = 0

predictionBlue = np.copy(prediction)
predictionBlue[:, :, 0] = 0
predictionBlue[:, :, 1] = 0

axs[1, 0].imshow(predictionRed)
axs[1, 1].imshow(predictionGreen)
axs[1, 2].imshow(predictionBlue)
plt.show()
