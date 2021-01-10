from ghost_scan.constants import filesCount

h = 660
w = 510

batchSize = 5
steps_per_epoch = 10

epochs = filesCount // (steps_per_epoch * batchSize)
