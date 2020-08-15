import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np

from .model import getModel, preprocess_input, loss
from .data_generator import getTensorFromFilepathPng

filename = sys.argv[1]

model = getModel()
model.load_weights('weights/my_model.h5')
X = getTensorFromFilepathPng('./data/printed_document/%s' % filename)
preprocessedX = preprocess_input(X)
groundTruth = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename)
prediction = model.predict(preprocessedX, steps=1)

print(loss(prediction, groundTruth))

fig, axs = plt.subplots(1, 3, figsize=(15, 8))
axs[0].imshow(preprocessedX.numpy()[0])
axs[1].imshow((prediction)[0])
axs[2].imshow(groundTruth.numpy()[0])
plt.show()
