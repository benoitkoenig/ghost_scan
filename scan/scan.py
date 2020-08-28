import matplotlib.pyplot as plt
import sys

from ghost_scan.scan.get_data import loadSingleUnresizedPngTensor
from ghost_scan.scan.remove_background.predict import predict as predictImageWithoutBackground
from ghost_scan.scan.get_carto_by_class.predict import predict as predictPositions
from ghost_scan.scan.get_a4.get_a4 import getA4

filename = [f for f in sys.argv if ((f[-3:] != '.py') & (f != '-v') & (f != '--validation'))][0]
isValidationData = ('-v' in sys.argv) | ('--validation' in sys.argv)

if isValidationData:
  inputImage = loadSingleUnresizedPngTensor('./data/validation_data/printed_document/%s' % filename)
else:
  inputImage = loadSingleUnresizedPngTensor('./data/printed_document/%s' % filename)
imageWithoutBackground = predictImageWithoutBackground(inputImage)
positions = predictPositions(imageWithoutBackground)
documentA4 = getA4(inputImage.numpy()[0], positions)

fig, ax = plt.subplots(1, 1, figsize=(50, 50))
ax.imshow(documentA4)
plt.show()
