import matplotlib.pyplot as plt
import sys

from ghost_scan.constants import dirpath
from ghost_scan.scan.get_data import loadSingleUnresizedPngTensor
from ghost_scan.scan.remove_background.predict import RemoveBackground
from ghost_scan.scan.detect_pose.predict import GetCartoByPoints
from ghost_scan.scan.get_a4.get_a4 import getA4

if ('-r' in sys.argv) | ('--real' in sys.argv):
  folderPath = '%s/data/real' % dirpath
elif ('-v' in sys.argv) | ('--validation' in sys.argv):
  folderPath = '%s/data/validation' % dirpath
else:
  folderPath = '%s/data/training' % dirpath

removeBackground = RemoveBackground()
getCartoByPoints = GetCartoByPoints()

while True:
  filename = input('Filename (empty to leave): ')
  if filename == '':
    break
  inputImage = loadSingleUnresizedPngTensor('%s/printed_document/%s' % (folderPath, filename)).numpy()
  removeBackgroundPreds, coords = removeBackground.predict(inputImage)
  positions = getCartoByPoints.predict(removeBackgroundPreds, coords, inputImage.shape)
  documentA4 = getA4(inputImage[0], positions)

  fig, axs = plt.subplots(1, 1, figsize=(50, 50))
  axs.imshow(documentA4)
  plt.show()
