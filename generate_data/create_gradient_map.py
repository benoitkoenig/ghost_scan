# This file is used to create the file gradient_map.png
# Since gradient_map.png is committed, this file only needs to be executed if you want to change it

import os
import png

width = 256 * 4
height = 256 * 4

imgRGB = [[(x * 64, y * 64, 65535) for x in range(width)] for y in range(height)] # imgRGB is of shape (height, width, 3)
img = [[item for sublist in row for item in sublist] for row in imgRGB] # img is the same as imgRGB, except it is of shape (height, width * 3)

with open('%s/gradient_map.png' % os.path.dirname(os.path.realpath(__file__)), 'wb') as f:
  w = png.Writer(width, height, greyscale=False, bitdepth=16)
  w.write(f, img)
