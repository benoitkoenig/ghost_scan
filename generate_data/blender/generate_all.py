import sys

from ghost_scan.generate_data.blender.generate_both_pictures import generate_both_pictures
from ghost_scan.constants import filenames, validationFilenames, dirpath

if ('-v' in sys.argv) | ('--validation' in sys.argv):
  folderpath = '%s/data/validation' % dirpath
  f = validationFilenames
else:
  folderpath = '%s/data/training' % dirpath
  f = filenames

for (index, filename) in enumerate(f):
  generate_both_pictures(
    inputPath='%s/png/%s' % (folderpath, filename),
    outputDocumentPath='%s/printed_document/%s' % (folderpath, filename),
    outputGradientPath='%s/printed_gradient_map/%s' % (folderpath, filename),
  )
  print('%s/%s' % (index + 1, len(f)))
