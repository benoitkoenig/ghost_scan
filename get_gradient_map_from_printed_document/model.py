import segmentation_models as sm
import tensorflow as tf

from .constants import h, w

BACKBONE = 'resnet34'
preprocess_input = sm.get_preprocessing(BACKBONE)
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)

def loss(gt, pr):
  # First, we remove pixels that aren't perfect green. Those pixels are in between the document and the background: we decide to exclude them
  # This could also be done in preprocessing
  [tensorRed, tensorGreen, tensorBlue] = tf.split(gt, 3, axis=3)
  tensorRed = tf.cast(tensorRed == 1, gt.dtype)
  tensorGreen = tensorRed * tensorGreen
  tensorBlue = tensorRed * tensorBlue
  gtWithoutFadingBorders = tf.concat([tensorRed, tensorGreen, tensorBlue], axis=3)

  # Second, all pixels in preds that are above, but should be one, are replaced by one. This is because a value above 1 in postprocessing will be replaced by 1 as well
  capToOne = tf.cast((gtWithoutFadingBorders == 1) & (pr > 1), dtype=pr.dtype)
  cappedPred = capToOne + (1 - capToOne) * pr

  # Finally, calculate MSE with both adapted values
  return tf.math.reduce_mean((gtWithoutFadingBorders - cappedPred) ** 2)

def getModel():
  model = sm.Unet(BACKBONE, input_shape=(h, w, 3), classes=3, activation='relu', weights=None, encoder_weights=None)
  model.compile(optimizer=optimizer, loss=loss)
  return model
