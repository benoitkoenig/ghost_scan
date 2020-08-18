import csv
import random

from ghost_scan.get_tensor_from_filepath import getTensorFromFilepathPng
from .preprocess import preprocessForTraining

def getFilesData():
  with open('data/printed_document_cartography.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    rows = [r for r in csvReader][1:]
  random.shuffle(rows)
  return rows

def getDataGenerator():
  files = getFilesData()
  for [filename, positions] in files:
    rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, keepAlphaChannel=True)
    X, Y = preprocessForTraining(rawX, eval(positions))
    yield X, Y

def getSingleEntry(filename):
  files = getFilesData()
  [[_, positions]] = [f for f in getFilesData() if f[0] == filename]
  rawX = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, keepAlphaChannel=True)
  X, Y = preprocessForTraining(rawX, eval(positions))
  return X, Y
