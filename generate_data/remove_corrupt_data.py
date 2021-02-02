import numpy as np
import cv2
import os

from ghost_scan.constants import dirpath, filenames, validationFilenames

def checkPicture(filepath):
  data = np.array(cv2.imread(filepath, cv2.IMREAD_UNCHANGED))
  assert len(data.shape) == 3
  assert data.shape[0] > 5
  assert data.shape[1] > 5
  assert (data.shape[2] == 3 or data.shape[2] == 4)

def removeCorruptData(folder='training'):
  if (folder == 'training'):
    allFiles = filenames
  if (folder == 'validation'):
    allFiles = validationFilenames
  for (i, filename) in enumerate(allFiles):
    try:
      checkPicture('%s/data/%s/png/%s' % (dirpath, folder, filename))
      checkPicture('%s/data/%s/printed_document/%s' % (dirpath, folder, filename))
      checkPicture('%s/data/%s/printed_gradient_map/%s' % (dirpath, folder, filename))
      print('%s/%s' % (i, len(allFiles)), end='\r')
    except KeyboardInterrupt:
      exit(0)
    except:
      print('\033[91m[Error] Deleting %s' % filename, '\033[0m')
      os.remove('%s/data/%s/png/%s' % (dirpath, folder, filename))
      os.remove('%s/data/%s/printed_document/%s' % (dirpath, folder, filename))
      os.remove('%s/data/%s/printed_gradient_map/%s' % (dirpath, folder, filename))

print('Checking training data')
removeCorruptData('training')
print('Checking validation data')
removeCorruptData('validation')
