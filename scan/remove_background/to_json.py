import tensorflowjs as tfjs

from ghost_scan.constants import dirpath
from .model import getModel

model = getModel(weights='%s/scan/weights/remove_background/weights' % dirpath)
tfjs.converters.save_keras_model(model, '%s/scan/exports_json/remove_background' % dirpath)
