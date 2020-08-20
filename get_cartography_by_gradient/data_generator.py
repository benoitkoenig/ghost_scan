from ghost_scan.getData import getFilesData, getTensorFromFilepathPng
from .constants import h, w

def getDataGenerator():
  for [filename, _] in getFilesData():
    X = getTensorFromFilepathPng('./data/printed_document_without_background/%s' % filename, h, w, keepAlphaChannel=True)
    Y = getTensorFromFilepathPng('./data/printed_gradient_map/%s' % filename, h, w)
    yield X, Y, [None]
