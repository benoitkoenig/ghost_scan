from ghost_scan.generate_data.blender.generate_both_pictures import generate_both_pictures
from ghost_scan.constants import filenames, dirpath

for (index, filename) in enumerate(filenames):
  generate_both_pictures(
    inputPath='%s/data/png/%s' % (dirpath, filename),
    outputDocumentPath='%s/data/printed_document/%s' % (dirpath, filename),
    outputGradientPath='%s/data/printed_gradient_map/%s' % (dirpath, filename),
  )
  print('%s/%s' % (index + 1, len(filenames)))