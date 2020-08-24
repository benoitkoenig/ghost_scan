from ghost_scan.constants import filesCount

h = 256
w = 256

validationSize = 100
batchSize = 10
steps_per_epoch = 5

epochs = (filesCount - validationSize) // (steps_per_epoch * batchSize)
