import matplotlib.pyplot as plt
import sys

from ghost_scan.scan.get_data import loadSingleUnresizedPngTensor
from ghost_scan.scan.remove_background.predict import RemoveBackground
from ghost_scan.scan.get_carto_by_points.predict import GetCartoByPoints
from ghost_scan.scan.get_a4.get_a4 import getA4

isValidationData = ('-v' in sys.argv) | ('--validation' in sys.argv)

removeBackground = RemoveBackground()
getCartoByPoints = GetCartoByPoints()

while True:
  filename = input('Filename (empty to leave): ')
  if filename == '':
    break
  if isValidationData:
    inputImage = loadSingleUnresizedPngTensor('./data/validation_data/printed_document/%s' % filename).numpy()
  else:
    inputImage = loadSingleUnresizedPngTensor('./data/printed_document/%s' % filename).numpy()
  removeBackgroundPreds, coords = removeBackground.predict(inputImage)
  positions = getCartoByPoints.predict(removeBackgroundPreds, coords, inputImage.shape)
  documentA4 = getA4(inputImage[0], positions)

  fig, axs = plt.subplots(1, 4, figsize=(50, 50))
  axs[0].imshow(inputImage[0])
  axs[1].imshow(removeBackgroundPreds[0, :, :, 0])
  axs[2].imshow(inputImage[0])
  axs[2].plot(positions[:, 1], positions[:, 0], marker='x')
  axs[3].imshow(documentA4)
  plt.show()
