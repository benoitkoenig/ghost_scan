import bpy
import bmesh
import math
import random
import sys

from .initialize_scene import initialize_scene
from .create_mesh import create_document, create_background
from .prepare_gradient_picture import prepare_gradient_picture
from .save_picture import save_picture

def main():
  filename = sys.argv[5]
  folderPath = sys.argv[6]

  initialize_scene()
  create_document('%s/data/png/%s' % (folderPath, filename))
  create_background()

  save_picture('%s/data/printed_document/%s' % (folderPath, filename))

  prepare_gradient_picture()
  save_picture('%s/data/printed_gradient_map/%s' % (folderPath, filename))

if __name__ == '__main__':
  main()
