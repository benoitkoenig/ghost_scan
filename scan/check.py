import matplotlib.pyplot as plt
import sys

from ghost_scan.constants import dirpath
from ghost_scan.scan.get_data import loadSingleUnresizedPngTensor
from ghost_scan.scan.remove_background.predict import RemoveBackground
from ghost_scan.scan.get_carto_by_points.predict import GetCartoByPoints
from ghost_scan.scan.get_a4.get_a4 import getA4

isValidationData = ('-r' in sys.argv) | ('--real' in sys.argv)

removeBackground = RemoveBackground()
getCartoByPoints = GetCartoByPoints()

while True:
  filename = input('Filename (empty to leave): ')
  if filename == '':
    break
  if isValidationData:
    inputImage = loadSingleUnresizedPngTensor('%s/data/real/printed_document/%s' % (dirpath, filename)).numpy()
  else:
    inputImage = loadSingleUnresizedPngTensor('%s/data/training/printed_document/%s' % (dirpath, filename)).numpy()
  removeBackgroundPreds, coords = removeBackground.predict(inputImage)
  positions = getCartoByPoints.predict(removeBackgroundPreds, coords, inputImage.shape)
  documentA4 = getA4(inputImage[0], positions)

  fig, axs = plt.subplots(1, 1, figsize=(50, 50))
  axs.imshow(documentA4)
  plt.show()
