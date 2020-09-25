from ghost_scan.constants import filesCount

h = 165
w = 127

batchSize = 1
steps_per_epoch = 50

epochs = filesCount // (steps_per_epoch * batchSize)
