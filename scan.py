import matplotlib.pyplot as plt
import sys

from ghost_scan.get_data import getTensorFromFilepathPng
from ghost_scan.remove_background.predict import predict as predictImageWithoutBackground
from ghost_scan.get_carto_by_class.predict import predict as predictPositions
from ghost_scan.get_a4.predict import predict as predictDocumentA4

filename = sys.argv[1]

inputImage = getTensorFromFilepathPng('./data/printed_document/%s' % filename)
imageWithoutBackground = predictImageWithoutBackground(inputImage)
positions = predictPositions(imageWithoutBackground)
documentA4 = predictDocumentA4(imageWithoutBackground, positions)

fig, ax = plt.subplots(1, 1, figsize=(50, 50))
ax.imshow(documentA4[0])
plt.show()
