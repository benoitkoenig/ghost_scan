import matplotlib.pyplot as plt
import sys
import tensorflow as tf

from .data_generator import getSingleEntry
from .model import getModel

filename = sys.argv[1]

model = getModel()
model.load_weights('./weights/get_a4')
X, Y = getSingleEntry(filename)
pred = model.predict(X, steps=1)

print('Loss: %s' % tf.keras.losses.MeanSquaredError()(Y, pred).numpy())

fig, ax = plt.subplots(1, 2, figsize=(50, 50))
ax[0].imshow(Y.numpy()[0])
ax[1].imshow(pred[0])
plt.show()
