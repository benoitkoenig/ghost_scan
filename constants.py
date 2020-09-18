import os

coords = [
  (0.00, 0.00), (0.00, 0.25), (0.00, 0.50), (0.00, 0.75), (0.00, 1.00),
  (0.25, 0.00), (0.25, 0.25), (0.25, 0.50), (0.25, 0.75), (0.25, 1.00),
  (0.50, 0.00), (0.50, 0.25), (0.50, 0.50), (0.50, 0.75), (0.50, 1.00),
  (0.75, 0.00), (0.75, 0.25), (0.75, 0.50), (0.75, 0.75), (0.75, 1.00),
  (1.00, 0.00), (1.00, 0.25), (1.00, 0.50), (1.00, 0.75), (1.00, 1.00),
]
numberOfPoints = len(coords)

dirpath = os.path.dirname(os.path.realpath(__file__))
filenames = [f for f in os.listdir('%s/data/training/png' % dirpath) if (f[-4:] == '.png')]
filesCount = len(filenames)
validationFilenames = [f for f in os.listdir('%s/data/validation/png' % dirpath) if (f[-4:] == '.png')]
validationFilesCount = len(validationFilenames)

h = 256
w = 256
