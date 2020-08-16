import csv
import numpy as np
import os
from PIL import Image

coords = [
  (0, 0), (0, 128), (0, 256),
  (128, 0), (128, 128), (128, 256),
  (256, 0), (256, 128), (256, 256),
]

allPositions = []
for filename in os.listdir('./data/printed_gradient_map'):
  if filename[-4:] != '.png':
    continue
  imgRGBA = Image.open('./data/printed_gradient_map/%s' % filename)
  imgRGB = imgRGBA.convert('RGB')
  data = np.asarray(imgRGB, dtype=np.int32)
  [red, green, blue] = np.dsplit(data, 3)

  red = (red == 255).astype(red.dtype)
  green = red * green + (1 - red) * 1000
  blue = red * blue + (1 - red) * 1000


  squareDistanceMatrices = [(green - c[0]) ** 2 + (blue - c[1]) ** 2 for c in coords]
  positions = [np.unravel_index(np.argmin(s, axis=None), s.shape) for s in squareDistanceMatrices]
  positions = np.array(positions)[:, 0:2].tolist()
  allPositions.append([filename, positions])

with open('./data/printed_document_cartography.csv', 'w') as csvFile:
  csvWriter = csv.writer(csvFile, delimiter=',')
  csvWriter.writerow(['filename', coords])
  for [filename, positions] in allPositions:
    csvWriter.writerow([filename, positions])
