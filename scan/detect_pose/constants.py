from ghost_scan.constants import filesCount

batchSize = 10
steps_per_epoch = 5

epochs = filesCount // (steps_per_epoch * batchSize)
