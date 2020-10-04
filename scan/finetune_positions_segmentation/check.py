import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import sys
import tensorflow as tf

from ghost_scan.constants import coords, dirpath
from ghost_scan.scan.get_a4.get_a4 import getA4
from .constants import h, w
from .get_data import getXY
from .model import getModel

coordsNp = np.array(coords)

filename = sys.argv[1]

X, Y = getXY([filename])
model = getModel(weights='%s/scan/models/weights/finetune_positions/weights' % dirpath)
preds = model.predict(X, steps=1)

XtoDisplay = X.numpy()[0]

YtoDisplay = Y.numpy()[0]
YtoDisplay = YtoDisplay * (YtoDisplay > 3).astype(np.float32)
YtoDisplay = np.sum(YtoDisplay, axis=-1)

predsToDisplay = np.sum(preds[0], axis=-1)

fig, axs = plt.subplots(1, 3, figsize=(50, 50))

axs[0].set_title('Input picture')
axs[0].imshow(XtoDisplay)

axs[1].set_title('Y')
axs[1].imshow(YtoDisplay)

axs[2].set_title('Preds')
axs[2].imshow(predsToDisplay)

plt.show()
