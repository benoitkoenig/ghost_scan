import math
import numpy as np
import tensorflow as tf

from .constants import h, w, inputChannels

def calculatePosition(inputPositions, destinationY, destinationX):
  if (destinationX + destinationY < 1):
    vectorY = inputPositions[2] - inputPositions[0]
    vectorX = inputPositions[1] - inputPositions[0]
    [originY, originX] = inputPositions[0] + (destinationY * vectorY + destinationX * vectorX)
  else:
    vectorY = inputPositions[1] - inputPositions[3]
    vectorX = inputPositions[2] - inputPositions[3]
    [originY, originX] = inputPositions[3] + ((1 - destinationY) * vectorY + (1 - destinationX) * vectorX)

  originYInt = int(round(originY))
  originXInt = int(round(originX))
  return originYInt, originXInt, originY - originYInt, originX - originXInt

def getXChannels(positions, y, x, inputData):
  originY, originX, deviationY, deviationX = calculatePosition(positions, y, x)
  pixelData = inputData[originY - 1: originY + 2, originX - 1: originX + 2, :]
  channels = np.concatenate([pixelData.flatten(), [deviationY, deviationX]])
  return channels

def preprocess(inputTensor, inputPositions):
  inputData = inputTensor.numpy()[0]
  positions = np.array(inputPositions)
  outputData = [[getXChannels(positions, destinationY / h, destinationX / w, inputData) for destinationX in range(w)] for destinationY in range(h)]
  X = tf.convert_to_tensor([outputData])
  return X