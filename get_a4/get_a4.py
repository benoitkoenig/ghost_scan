import numpy as np

from .constants import h, w

def calculatePosition(positions, destinationY, destinationX):
  if (destinationX + destinationY < 1):
    vectorY = positions[2] - positions[0]
    vectorX = positions[1] - positions[0]
    [originY, originX] = positions[0] + (destinationY * vectorY + destinationX * vectorX)
  else:
    vectorY = positions[1] - positions[3]
    vectorX = positions[2] - positions[3]
    [originY, originX] = positions[3] + ((1 - destinationY) * vectorY + (1 - destinationX) * vectorX)

  return int(round(originY)), int(round(originX))

def getChannels(positions, destinationY, destinationX, inputData):
  originY, originX = calculatePosition(positions, destinationY, destinationX)
  pixelData = inputData[originY, originX, 0:3]
  return pixelData

def getA4(inputData, inputPositions):
  positions = np.array(inputPositions)
  outputData = [[getChannels(positions, destinationY / h, destinationX / w, inputData) for destinationX in range(w)] for destinationY in range(h)]
  return outputData
