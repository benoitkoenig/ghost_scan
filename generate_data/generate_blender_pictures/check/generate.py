import os
import sys

from ghost_scan.generate_data.generate_blender_pictures.initialize_scene import initialize_scene
from ghost_scan.generate_data.generate_blender_pictures.create_mesh import create_document, create_background
from ghost_scan.generate_data.generate_blender_pictures.prepare_gradient_picture import prepare_gradient_picture
from ghost_scan.generate_data.generate_blender_pictures.save_picture import save_picture

dirpath = os.path.dirname(__file__)

def check():
  initialize_scene()
  create_document('%s/input.png' % dirpath)
  create_background()

  save_picture('%s/printed_document.png' % dirpath)

  prepare_gradient_picture()
  save_picture('%s/printed_gradient_map.png' % dirpath)

try:
  check()
except Exception as e:
  print(e)
  sys.exit(1)
