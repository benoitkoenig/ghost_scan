import bpy
import math
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

  scene.camera.location = [centered_random(), centered_random(), 10 + centered_random()]
  scene.camera.rotation_euler = [math.pi * centered_random() / 36, math.pi * centered_random() / 36, math.pi * (centered_random() / 36 - 0.5)]

def set_random_lightning():
  dataLamp = bpy.data.lamps[0]
  dataLamp.color = [1 - 0.5 * random.random() for _ in range(3)]
  dataLamp.distance = 20
  dataLamp.type = random.choice(['POINT', 'SUN', 'SPOT', 'HEMI', 'AREA'])
  if (dataLamp.type == 'POINT') | (dataLamp.type == 'SPOT'):
    dataLamp.energy = 10
  if (dataLamp.type == 'AREA'):
    dataLamp.energy = 0.5

  objLamp = [o for o in bpy.context.scene.objects if o.type == 'LAMP'][0]
  objLamp.location = [10 * centered_random(), 10 * centered_random(), 18 + 5 * centered_random()]
  objLamp.rotation_euler = [math.pi * centered_random() / 36, math.pi * centered_random() / 36, math.pi * (centered_random() / 36 - 0.5)]


def set_render_params():
  scene = bpy.data.scenes[0]
  scene.render.image_settings.color_depth = '16'
  scene.render.image_settings.file_format = 'PNG'
  bpy.context.scene.render.resolution_x = 600 + int(200 * centered_random())
  bpy.context.scene.render.resolution_y = 600 + int(200 * centered_random())

def initialize_scene():
  delete_default_cube()
  move_camera()
  set_random_lightning()
  set_render_params()
