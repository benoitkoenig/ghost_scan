import csv
import math
import numpy as np
import PIL
import random
import tensorflow as tf

def resize(inputTensor, height, width):
  [_, inputH, inputW, _] = inputTensor.shape
  if (inputH > height) | (inputW > width):
    factor = min(height / inputH, width / inputW)
    newH = int(inputH * factor)
    newW = int(inputW * factor)
    downsizedTensor = tf.image.resize(inputTensor, (newH, newW))
  else:
    downsizedTensor = inputTensor

  [_, downsizedH, downsizedW, _] = downsizedTensor.shape
  paddingHBefore = (height - downsizedH) // 2
  paddingHAfter = math.ceil((height - downsizedH) / 2)
  paddingWBefore = (width - downsizedW) // 2
  paddingWAfter = math.ceil((width - downsizedW) / 2)
  resizedTensor = tf.pad(downsizedTensor, [(0, 0), (paddingHBefore, paddingHAfter), (paddingWBefore, paddingWAfter), (0, 0)])

  return resizedTensor

def getTensorFromFilepathPng(filepath, height=None, width=None, keepAlphaChannel=False):
  img = PIL.Image.open(filepath)
  if (keepAlphaChannel == False):
    img = img.convert('RGB')
  data = np.asarray(img) / 255
  tensor = tf.convert_to_tensor([data])
  if (height != None) & (width != None):
    tensor = resize(tensor, height, width)
  return tensor

def getFilesData():
  with open('data/printed_document_cartography.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    rows = [[r[0], eval(r[1])] for r in csvReader][1:]
  random.shuffle(rows)
  return rows

def getPositions(filename):
  matchingFiles = [f for f in getFilesData() if f[0] == filename]
  assert (len(matchingFiles) != 0), 'File not found'
  return matchingFiles[0][1]
