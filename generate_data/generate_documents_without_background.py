import numpy as np
import cv2
import png

from ghost_scan.constants import dirpath, filenames

for index, filename in enumerate(filenames):
  rawImg = np.array(cv2.imread('%s/data/training/printed_document/%s' % (dirpath, filename), cv2.IMREAD_UNCHANGED))
  rawGrad = np.array(cv2.imread('%s/data/training/printed_gradient_map/%s' % (dirpath, filename), cv2.IMREAD_UNCHANGED))
  img = np.asarray(rawImg)
  grad = np.asarray(rawGrad)
  [blue, _, _, _] = np.dsplit(grad, 4)
  mask = (blue == 65535)
  rgbaMask = np.concatenate([mask, mask, mask, mask], axis=2)
  newImgUnreshaped = rgbaMask * img
  [height, width, _] = newImgUnreshaped.shape
  newImg = newImgUnreshaped.reshape((height, width * 4))
  with open('%s/data/training/printed_document_without_background/%s' % (dirpath, filename), 'wb') as f:
    w = png.Writer(width, height, greyscale=False, alpha=True, bitdepth=16)
    w.write(f, newImg)
  print('%s/%s' % (index + 1, len(filenames)), end='\r')
