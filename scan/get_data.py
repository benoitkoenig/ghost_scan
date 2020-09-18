import csv
import cv2
import numpy as np
import random
import tensorflow as tf

from ghost_scan.constants import dirpath, filenames, validationFilenames

def getFilenames(folder='training'):
  if (folder == 'validation'):
    filenamesCopy = [f for f in validationFilenames]
  else:
    filenamesCopy = [f for f in filenames]
  random.shuffle(filenamesCopy)
  return filenamesCopy

positionsRows = None
def getPositions(filename, folder='training'):
  global positionsRows
  if positionsRows == None:
    with open('%s/data/%s/printed_document_carto.csv' % (dirpath, folder)) as csvFile:
      csvReader = csv.reader(csvFile, delimiter=',')
      positionsRows = [[r[0], r[1]] for r in csvReader][1:]
  matchingFiles = [r[1] for r in positionsRows if r[0] == filename]
  assert (len(matchingFiles) != 0), 'File not found'
  return eval(matchingFiles[0])

def loadSingleUnresizedPngTensor(filepath):
  data = np.array(cv2.imread(filepath, cv2.IMREAD_UNCHANGED))
  data = data.astype(np.float32) / (65535 if data.dtype == 'uint16' else 255)
  tensor = tf.convert_to_tensor([data])
  if (tensor.shape[3] == 3):
    tensor = tf.pad(tensor, [(0, 0), (0, 0), (0, 0), (0, 1)], constant_values=1)
  return tensor

def loadPngTensors(filepaths, height, width):
  data = [np.array(cv2.imread(f, cv2.IMREAD_UNCHANGED)) for f in filepaths]
  data = [d.astype(np.float32) / (65535 if d.dtype == 'uint16' else 255) for d in data]
  tensors = [tf.convert_to_tensor(d) for d in data]
  resizedTensors = [tf.image.resize_with_pad(t, height, width) for t in tensors]
  tensor = tf.stack(resizedTensors)
  return tensor
