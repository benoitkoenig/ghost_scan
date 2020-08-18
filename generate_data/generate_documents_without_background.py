import numpy as np
import os
from PIL import Image
import png

dirpath = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir('%s/../data/printed_document' % dirpath):
  if filename[-4:] != '.png':
    continue
  rawImg = Image.open('%s/../data/printed_document/%s' % (dirpath, filename))
  rawGrad = Image.open('%s/../data/printed_gradient_map/%s' % (dirpath, filename))
  img = np.asarray(rawImg)
  grad = np.asarray(rawGrad)
  [redPixel, _, _, _] = np.dsplit(grad, 4)
  mask = (redPixel == 255)
  rgbaMask = np.concatenate([mask, mask, mask, mask], axis=2)
  newImgUnreshaped = rgbaMask * img
  [height, width, _] = newImgUnreshaped.shape
  newImg = newImgUnreshaped.reshape((height, width * 4))
  with open('%s/../data/printed_document_without_background/%s' % (dirpath, filename), 'wb') as f:
    w = png.Writer(width, height, greyscale=False, alpha=True)
    w.write(f, newImg)
  print(filename)
