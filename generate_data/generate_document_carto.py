import csv
import numpy as np
import os
from PIL import Image

from ghost_scan.constants import coords

dirpath = os.path.dirname(os.path.realpath(__file__))

allPositions = []
for filename in os.listdir('%s/../data/printed_gradient_map' % dirpath):
  if filename[-4:] != '.png':
    continue
  imgRGBA = Image.open('%s/../data/printed_gradient_map/%s' % (dirpath, filename))
  imgRGB = imgRGBA.convert('RGB')
  data = np.asarray(imgRGB, dtype=np.int32)
  [red, green, blue] = np.dsplit(data, 3)

  red = (red == 255).astype(red.dtype)
  green = red * green + (1 - red) * 1000
  blue = red * blue + (1 - red) * 1000

  squareDistanceMatrices = [(green - c[0]) ** 2 + (blue - c[1]) ** 2 for c in coords]
  positions = [np.unravel_index(np.argmin(s, axis=None), s.shape) for s in squareDistanceMatrices]
  positions = np.array(positions)[:, 0:2]
  positions = positions.tolist()
  allPositions.append([filename, positions])
  print(filename)

with open('%s/../data/printed_document_carto.csv' % dirpath, 'w') as csvFile:
  csvWriter = csv.writer(csvFile, delimiter=',')
  csvWriter.writerow(['filename', coords])
  for [filename, positions] in allPositions:
    csvWriter.writerow([filename, positions])
