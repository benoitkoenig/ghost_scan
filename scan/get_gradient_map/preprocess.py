import random
import tensorflow as tf

def preprocessTrainingOnly(inputX):
  [batchsize, _, _, nbChannels] = inputX.shape
  mask = [[random.random() > 0.1 for _ in range(nbChannels)] for _ in range(batchsize)]
  mask = [[1, 1, 1] if m == [0, 0, 0] else m for m in mask]
  transposedX = tf.transpose(inputX, (1, 2, 0, 3))
  maskedX = mask * transposedX
  outputX = tf.transpose(maskedX, (2, 0, 1, 3))
  return outputX
