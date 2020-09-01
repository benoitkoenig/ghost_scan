import bpy
import os

from ghost_scan.generate_data.blender.generate_both_pictures import generate_both_pictures

dirpath = os.path.dirname(__file__)

while (True):
  generate_both_pictures(
    inputPath='%s/input.png' % dirpath,
    outputDocumentPath='%s/printed_document.png' % dirpath,
    outputGradientPath='%s/printed_gradient_map.png' % dirpath,
  )
  bpy.ops.wm.save_as_mainfile(filepath='%s/scene.blend' % dirpath)

  # This file is called in blender context. Importing matplotlib after doing the blender stuff works well - importing it at the beginning of the file results in issues
  import matplotlib.pyplot as plt
  import matplotlib.image as mpimg

  img1 = mpimg.imread('%s/printed_document.png' % dirpath)
  img2 = mpimg.imread('%s/printed_gradient_map.png' % dirpath)

  fig, axs = plt.subplots(1, 2, figsize=(50, 50))
  axs[0].imshow(img1)
  axs[1].imshow(img2)
  plt.show()
