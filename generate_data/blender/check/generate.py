import os
import sys

from ghost_scan.generate_data.blender.generate_both_pictures import generate_both_pictures

try:
  dirpath = os.path.dirname(__file__)
  generate_both_pictures(
    inputPath='%s/input.png' % dirpath,
    outputDocumentPath='%s/printed_document.png' % dirpath,
    outputGradientPath='%s/printed_gradient_map.png' % dirpath,
  )
except Exception as e:
  print(e)
  sys.exit(1)
