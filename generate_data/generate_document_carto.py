import csv
import cv2
import numpy as np
import os

from ghost_scan.constants import coords

dirpath = os.path.dirname(os.path.realpath(__file__))
filenames = [f for f in os.listdir('%s/../data/printed_gradient_map' % dirpath) if (f[-4:] == '.png')]

allPositions = []
for index, filename in enumerate(filenames):
  data = np.array(cv2.imread('%s/../data/printed_gradient_map/%s' % (dirpath, filename), cv2.IMREAD_UNCHANGED), dtype=np.float32) / 65535

  [blue, green, red, _] = np.dsplit(data, 4)

  blue = (blue == 1).astype(blue.dtype)
  green = blue * green + (1 - blue) * 100
  red = blue * red + (1 - blue) * 100

  squareDistanceMatrices = [(green - c[0]) ** 2 + (red - c[1]) ** 2 for c in coords]
  positions = [np.unravel_index(np.argmin(s, axis=None), s.shape) for s in squareDistanceMatrices]
  positions = np.array(positions)[:, 0:2]
  positions = positions.tolist()
  allPositions.append([filename, positions])
  print('%s/%s' % (index + 1, len(filenames)), end='\r')

with open('%s/../data/printed_document_carto.csv' % dirpath, 'w') as csvFile:
  csvWriter = csv.writer(csvFile, delimiter=',')
  csvWriter.writerow(['filename', coords])
  for [filename, positions] in allPositions:
    csvWriter.writerow([filename, positions])
