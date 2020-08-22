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
  scene.camera.rotation_mode = 'XYZ'

  scene.camera.location.x = 1.485 + centered_random() / 10
  scene.camera.location.y = 1.05 + centered_random() / 10
  scene.camera.location.z = 10 + centered_random()

  scene.camera.rotation_euler[0] = math.pi * centered_random() / 36
  scene.camera.rotation_euler[1] = math.pi * centered_random() / 36
  scene.camera.rotation_euler[2] = math.pi * (centered_random() / 36 - 0.5)

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
