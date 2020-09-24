import matplotlib.pyplot as plt
import sys
import tensorflow as tf

from ghost_scan.constants import dirpath
from .get_data import getXY
from .loss import loss
from .model import getModel

filename = sys.argv[1]

X, Y = getXY([filename])
model = getModel(weights='%s/scan/models/weights/remove_background/weights' % dirpath)
preds = model.predict(X, steps=1)

print('Loss: %s' % loss(Y, tf.convert_to_tensor(preds)).numpy())

fig, ax = plt.subplots(1, 1, figsize=(50, 50))
ax.imshow(X.numpy()[0])
plt.show()
