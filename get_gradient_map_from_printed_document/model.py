import segmentation_models as sm
import tensorflow as tf

BACKBONE = 'resnet34'
preprocess_input = sm.backbones.get_preprocessing(BACKBONE)

model = sm.Unet(BACKBONE, input_shape=(None, None, 3), classes=3, activation='linear')
model.compile(
  'Adam',
  loss=tf.keras.losses.MeanSquaredError(), # TODO: we need a custom loss, that ignores the result for coordinates when out of the paper
)
