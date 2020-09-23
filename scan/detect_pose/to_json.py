import tensorflowjs as tfjs

from ghost_scan.constants import dirpath
from .model import getModel

model = getModel(weights='%s/scan/weights/detect_pose/weights' % dirpath)
tfjs.converters.save_keras_model(model, '%s/scan/exports_json/detect_pose' % dirpath)
