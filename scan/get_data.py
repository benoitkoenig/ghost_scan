import csv
import cv2
import numpy as np
import random
import tensorflow as tf

def getFilesData():
  with open('data/printed_document_carto.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    rows = [[r[0], eval(r[1])] for r in csvReader][1:]
  random.shuffle(rows)
  return rows

def getPositions(filename):
  matchingFiles = [f for f in getFilesData() if f[0] == filename]
  assert (len(matchingFiles) != 0), 'File not found'
  return matchingFiles[0][1]

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
