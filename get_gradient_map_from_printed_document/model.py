import segmentation_models as sm
import tensorflow as tf

from .constants import h, w
from .loss import loss

BACKBONE = 'resnet34'
preprocess_input = sm.get_preprocessing(BACKBONE)
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)

def getModel():
  model = sm.Unet(BACKBONE, input_shape=(h, w, 3), classes=3, activation='linear', weights=None, encoder_weights=None)
  model.compile(optimizer=optimizer, loss=loss)
  return model
