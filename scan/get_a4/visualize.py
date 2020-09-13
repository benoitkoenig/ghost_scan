import matplotlib.pyplot as plt
import numpy as np
import sys

from ghost_scan.constants import dirpath
from ghost_scan.scan.get_data import getPositions, loadSingleUnresizedPngTensor
from .get_a4 import getA4

filename = sys.argv[1]

positions = getPositions(filename)
imageTensor = loadSingleUnresizedPngTensor('%s/data/printed_document/%s' % (dirpath, filename))
a4Image = getA4(imageTensor.numpy()[0], positions)

fig, ax = plt.subplots(1, 1, figsize=(50, 50))
ax.imshow(a4Image)
plt.show()
