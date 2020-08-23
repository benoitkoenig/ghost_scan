import bpy

from .create_mesh import set_texture_image

def set_lighting_conditions_for_gradient_picture():
  bpy.data.lamps[0].energy = 0

  world = bpy.data.worlds['World']
  world.ambient_color = 0, 0, 0
  world.horizon_color = 0, 0, 0
  world.zenith_color = 0, 0, 0

  mat = bpy.data.materials.get('MatDocument')
  mat.emit = 1
  mat.ambient = 0
  mat.translucency = 0

def prepare_gradient_picture(folderPath):
  set_lighting_conditions_for_gradient_picture()
  set_texture_image('Document', '%s/generate_data/gradient_map.png' % folderPath)
