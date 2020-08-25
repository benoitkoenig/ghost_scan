import bpy
import os

from .create_mesh import set_texture_image

def set_lighting_conditions_for_gradient_picture():
  bpy.data.lamps[0].energy = 0

  world = bpy.data.worlds['World']
  world.ambient_color = 0, 0, 0
  world.horizon_color = 0, 0, 0
  world.zenith_color = 0, 0, 0

  matDocument = bpy.data.materials.get('MatDocument')
  matDocument.emit = 1
  matDocument.ambient = 0
  matDocument.translucency = 0

  matBackground = bpy.data.materials.get('MatBackground')
  matBackground.emit = 0
  matBackground.ambient = 0
  matBackground.translucency = 0

def prepare_gradient_picture():
  set_lighting_conditions_for_gradient_picture()
  set_texture_image('Document', '%s/../gradient_map.png' % os.path.dirname(__file__))
