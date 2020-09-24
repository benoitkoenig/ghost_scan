from ghost_scan.constants import filesCount

h = 165
w = 127

batchSize = 10
steps_per_epoch = 5

epochs = filesCount // (steps_per_epoch * batchSize)
