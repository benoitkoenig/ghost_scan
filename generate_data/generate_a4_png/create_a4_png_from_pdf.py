import numpy as np
import cv2
import os
import glob
import tempfile

tempPath = tempfile.mkdtemp()

def is_picture_valid(filepath):
  data = np.array(cv2.imread(filepath, cv2.IMREAD_UNCHANGED))
  if len(data.shape) != 3:
    return False
  if (data.shape[0] < 5) or (data.shape[1] < 5) or (data.shape[2] != 3 and data.shape[2] != 4):
    return False
  if abs(data.shape[0]/ data.shape[1] - 297 / 210) > 0.05: # Check that the format is roughly a4
    return False
  return True

def create_a4_png_from_pdf(filepath, destination, name):
  os.system('pdftoppm -png "%s" "%s/%s"' % (filepath, tempPath, name))
  filenames = [f for f in os.listdir(tempPath)]
  valid_files = 0
  for (i, filename) in enumerate(filenames):
    filepath = '%s/%s' % (tempPath, filename)
    if is_picture_valid(filepath):
      os.system('mv %s %s' % (filepath, destination))
      valid_files += 1
    else:
      os.remove(filepath)
  return valid_files
