import bpy
import bmesh
import math
import random
import sys

from .initialize_scene import initialize_scene
from .create_document import create_document, set_texture_image
from .prepare_gradient_picture import prepare_gradient_picture
from .save_picture import save_picture

def main():
  filename = sys.argv[5]
  folderPath = sys.argv[6]

  initialize_scene()
  create_document()

  set_texture_image('%s/data/png/%s' % (folderPath, filename))
  save_picture('%s/data/printed_document/%s' % (folderPath, filename))

  prepare_gradient_picture()
  set_texture_image('%s/generate_data/gradient_map.png' % folderPath)
  save_picture('%s/data/printed_gradient_map/%s' % (folderPath, filename))

if __name__ == '__main__':
  main()
