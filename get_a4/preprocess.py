import math
import numpy as np
import tensorflow as tf

from .constants import h, w, inputChannels

def calculatePosition(inputPositions, destinationY, destinationX):
  if (destinationX + destinationY < 1):
    vectorY = inputPositions[1] - inputPositions[0]
    vectorX = inputPositions[2] - inputPositions[0]
    [originY, originX] = inputPositions[0] + (destinationY * vectorY + destinationX * vectorX)
  else:
    vectorY = inputPositions[2] - inputPositions[3]
    vectorX = inputPositions[1] - inputPositions[3]
    [originY, originX] = inputPositions[3] + ((1 - destinationY) * vectorY + (1 - destinationX) * vectorX)

  originYInt = int(round(originY))
  originXInt = int(round(originX))
  return originYInt, originXInt, originY - originYInt, originX - originXInt

def getXChannels(positions, y, x, inputData):
  originY, originX, deviationY, deviationX = calculatePosition(positions, y, x)
  pixelData = inputData[originY: originY + 3, originX: originX + 3, :] # We dont start at originY - 1 because it is compensated by the padding of 1
  channels = np.concatenate([pixelData.flatten(), [deviationY, deviationX]])
  return channels

def preprocess(inputTensor, inputPositions):
  inputData = inputTensor.numpy()[0]
  data = np.pad(inputData, [(1, 1), (1, 1), (0, 0)])
  positions = np.array(inputPositions)
  outputData = [[getXChannels(positions, destinationY / h, destinationX / w, inputData) for destinationX in range(w)] for destinationY in range(h)]
  X = tf.convert_to_tensor([outputData])
  return X
