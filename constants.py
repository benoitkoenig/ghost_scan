import os

coords = [(0, 0), (0, 1), (1, 0), (1, 1)]
numberOfPoints = len(coords)

dirpath = os.path.dirname(os.path.realpath(__file__))
filenames = [f for f in os.listdir('%s/data/printed_gradient_map' % dirpath) if (f[-4:] == '.png')]
filesCount = len(filenames)
