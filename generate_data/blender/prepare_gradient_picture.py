import bpy
import os

from ghost_scan.constants import dirpath
from .create_mesh import add_texture

def prepare_gradient_picture():
  for lamp in bpy.data.lamps:
    lamp.energy = 0

  matDocument = bpy.data.materials.get('MatDocument')
  matDocument.emit = 1
  matDocument.ambient = 0
  matDocument.translucency = 0

  matBackground = bpy.data.materials.get('MatBackground')
  matBackground.emit = 0
  matBackground.ambient = 0
  matBackground.translucency = 0

  bpy.data.textures.remove(bpy.data.textures['TextureDocumentPage'])
  bpy.data.textures.remove(bpy.data.textures['TextureDocumentPaper'])
  add_texture('Document', 'GradientMap', '%s/generate_data/gradient_map.png' % dirpath)
