from ghost_scan.constants import filesCount

validationSize = 20
batchSize = 10
steps_per_epoch = 5

epochs = (filesCount - validationSize) // (steps_per_epoch * batchSize)
