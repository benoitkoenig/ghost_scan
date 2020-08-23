import bpy
import math
import mathutils
import random

def centered_random():
  return 2 * random.random() - 1

def delete_default_cube():
  bpy.data.objects['Cube'].select = True
  bpy.ops.object.delete()

def move_camera():
  scene = bpy.context.scene

  v3d = [area for area in bpy.context.window.screen.areas if area.type == 'VIEW_3D'][0]
  v3d.spaces[0].pivot_point = 'CURSOR'

  scene.camera.location = mathutils.Vector([centered_random(), centered_random(), 10 + centered_random()])
  scene.camera.rotation_euler = mathutils.Vector([math.pi * centered_random() / 36, math.pi * centered_random() / 36, math.pi * (centered_random() / 36 - 0.5)])

def set_render_params():
  scene = bpy.data.scenes[0]
  scene.render.image_settings.color_depth = '16'
  scene.render.image_settings.file_format = 'PNG'
  bpy.context.scene.render.resolution_x = 600 + int(200 * centered_random())
  bpy.context.scene.render.resolution_y = 600 + int(200 * centered_random())

def initialize_scene():
  delete_default_cube()
  move_camera()
  set_render_params()
