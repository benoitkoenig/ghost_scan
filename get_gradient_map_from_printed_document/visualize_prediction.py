import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from .model import getModel, preprocess_input
from .data_generator import getTensorFromFilepathPng
from .loss import loss

filename = sys.argv[1]

model = getModel()
model.load_weights('weights/my_model.h5')
X = getTensorFromFilepathPng('./data/printed_document/%s' % filename)
preprocessedX = preprocess_input(X)
groundTruth = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename)
rawPrediction = model.predict(preprocessedX, steps=1)

print('Loss: %s' % loss(rawPrediction, groundTruth).numpy())

prediction = np.clip(rawPrediction[0], 0, 1)

fig, axs = plt.subplots(2, 3, figsize=(50, 50))
axs[0, 0].imshow(preprocessedX.numpy()[0])
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
