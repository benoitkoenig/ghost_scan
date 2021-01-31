import numpy as np

from .deviations import generateDeviations, getGradientFromDeviations, getDeviationsFromGradients

deviations = generateDeviations()
gradients = getGradientFromDeviations(deviations)
reconstructedDeviations = getDeviationsFromGradients(gradients)

assert np.all(deviations - reconstructedDeviations == 0)
