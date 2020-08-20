from ghost_scan.getData import getFilesData, getTensorFromFilepathPng
from .constants import h, w

def getGroundTruth(filename):
  transparentImageTensor = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, h, w, keepAlphaChannel=True)
  alphaChannel = transparentImageTensor[:, :, :, 3]
  return alphaChannel

def getDataGenerator():
  for [filename, _] in getFilesData():
    X = getTensorFromFilepathPng('./data/printed_document/%s' % filename, h, w)
    Y = getGroundTruth(filename)
    yield X, Y, [None]
