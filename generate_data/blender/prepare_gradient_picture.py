import bpy
import os

from .create_mesh import set_texture_image

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

  tex = bpy.data.textures['TextureDocument']
  tex.factor_red = 1
  tex.factor_green = 1
  tex.factor_blue = 1

  set_texture_image('Document', '%s/../gradient_map.png' % os.path.dirname(__file__))
