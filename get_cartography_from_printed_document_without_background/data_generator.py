import math
import numpy as np
import csv
import PIL
import random
import tensorflow as tf

from .constants import h, w, numberOfPoints

def getFilesData():
  with open('data/printed_document_cartography.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    rows = [r for r in csvReader][1:]
  return rows

def getTensorFromFilepathPng(filepath):
  img = PIL.Image.open(filepath)
  data = np.asarray(img) / 255
  tensor = tf.convert_to_tensor([data])
  return tensor

def resize(inputX, inputPositions):
  [_, inputH, inputW, _] = inputX.shape
  if (inputH > h) | (inputW > w):
    factor = min(h / inputH, w / inputW)
    newH = int(inputH * factor)
    newW = int(inputW * factor)
    downsizedX = tf.image.resize(inputX, (newH, newW))
  else:
    downsizedX = inputX

  [_, downsizedH, downsizedW, _] = downsizedX.shape
  paddingHBefore = (h - downsizedH) // 2
  paddingHAfter = math.ceil((h - downsizedH) / 2)
  paddingWBefore = (w - downsizedW) // 2
  paddingWAfter = math.ceil((w - downsizedW) / 2)
  resizedX = tf.pad(downsizedX, [(0, 0), (paddingHBefore, paddingHAfter), (paddingWBefore, paddingWAfter), (0, 0)])

  positions = inputPositions * factor
  positions = positions + [paddingHBefore, paddingWBefore]
  positions = positions * [1 / h, 1 / w]
  positions = [item for sublist in positions for item in sublist]
  resizedY = tf.convert_to_tensor([positions])

  return resizedX, resizedY

def getDataGenerator():
  files = getFilesData()
  random.shuffle(files)
  for [filename, positions] in files:
    unresizedX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename)
    X, Y = resize(unresizedX, np.array(eval(positions)))
    yield X, Y

def getSingleEntry(filename):
  files = getFilesData()
  [[_, positions]] = [f for f in getFilesData() if f[0] == filename]
  unresizedX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename)
  X, Y = resize(unresizedX, np.array(eval(positions)))
  return X, Y
