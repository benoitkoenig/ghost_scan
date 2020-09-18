import numpy as np
import cv2
import png
import sys

from ghost_scan.constants import dirpath, filenames, validationFilenames

if ('-v' in sys.argv) | ('--validation' in sys.argv):
  folderpath = '%s/data/validation' % dirpath
  f = validationFilenames
else:
  folderpath = '%s/data/training' % dirpath
  f = filenames

for index, filename in enumerate(f):
  rawImg = np.array(cv2.imread('%s/printed_document/%s' % (folderpath, filename), cv2.IMREAD_UNCHANGED))
  rawGrad = np.array(cv2.imread('%s/printed_gradient_map/%s' % (folderpath, filename), cv2.IMREAD_UNCHANGED))
  img = np.asarray(rawImg)
  grad = np.asarray(rawGrad)
  [blue, _, _, _] = np.dsplit(grad, 4)
  mask = (blue == 65535)
  rgbaMask = np.concatenate([mask, mask, mask, mask], axis=2)
  newImgUnreshaped = rgbaMask * img
  [height, width, _] = newImgUnreshaped.shape
  newImg = newImgUnreshaped.reshape((height, width * 4))
  with open('%s/printed_document_without_background/%s' % (folderpath, filename), 'wb') as openFile:
    w = png.Writer(width, height, greyscale=False, alpha=True, bitdepth=16)
    w.write(openFile, newImg)
  print('%s/%s' % (index + 1, len(f)), end='\r')
