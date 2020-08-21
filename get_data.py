import csv
import numpy as np
import PIL
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

def getTensorFromFilepathPng(filepath):
  img = PIL.Image.open(filepath)
  data = np.asarray(img) / 255
  tensor = tf.convert_to_tensor([data])
  return tensor
