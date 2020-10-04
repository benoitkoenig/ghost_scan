from ghost_scan.constants import filesCount

h = 160
w = 128

batchSize = 10
steps_per_epoch = 5

epochs = filesCount // (steps_per_epoch * batchSize)
