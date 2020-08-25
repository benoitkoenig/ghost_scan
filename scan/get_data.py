import csv
import cv2
import numpy as np
import random
import tensorflow as tf

from ghost_scan.constants import filenames

def getFilenames():
  filenamesCopy = [f for f in filenames]
  random.shuffle(filenamesCopy)
  return filenamesCopy

positionsRows = None
def getPositions(filename):
  global positionsRows
  if positionsRows == None:
    with open('data/printed_document_carto.csv') as csvFile:
      csvReader = csv.reader(csvFile, delimiter=',')
      positionsRows = [[r[0], r[1]] for r in csvReader][1:]
  matchingFiles = [r[1] for r in positionsRows if r[0] == filename]
  assert (len(matchingFiles) != 0), 'File not found'
  return eval(matchingFiles[0])

def loadSingleUnresizedPngTensor(filepath):
  data = np.array(cv2.imread(filepath, cv2.IMREAD_UNCHANGED), dtype=np.float32) / 65535
  tensor = tf.convert_to_tensor([data])
  return tensor

def loadPngTensors(filepaths, height, width):
  data = [np.array(cv2.imread(f, cv2.IMREAD_UNCHANGED), dtype=np.float32) / 65535 for f in filepaths]
  tensors = [tf.convert_to_tensor(d) for d in data]
  resizedTensors = [tf.image.resize_with_pad(t, height, width) for t in tensors]
  tensor = tf.stack(resizedTensors)
  return tensor
