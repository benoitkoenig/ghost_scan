import os
import sys

from ghost_scan.generate_data.blender.generate_both_pictures import generate_both_pictures

filename = sys.argv[5]

dirname = os.path.dirname(__file__)

generate_both_pictures(
  inputPath='%s/../../data/png/%s' % (dirname, filename),
  outputDocumentPath='%s/../../data/printed_document/%s' % (dirname, filename),
  outputGradientPath='%s/../../data/printed_gradient_map/%s' % (dirname, filename),
)
