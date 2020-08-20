import csv
import random

from ghost_scan.getData import getTensorFromFilepathPng
from .preprocess import preprocess, preprocessPositions

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
    X, coords = preprocess(rawX)
    Y = preprocessPositions(eval(positions), coords)
    yield X, Y

def getSingleEntry(filename):
  files = getFilesData()
  [[_, positions]] = [f for f in getFilesData() if f[0] == filename]
  originalImage = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, keepAlphaChannel=True)
  X, coords = preprocess(originalImage)
  originalPositions = eval(positions)
  Y = preprocessPositions(originalPositions, coords)
  return originalImage, originalPositions, X, Y, coords
