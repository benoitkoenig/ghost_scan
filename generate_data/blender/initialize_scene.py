import bpy
import math
import mathutils
import random

def centered_random():
  return 2 * random.random() - 1

def delete_default():
  bpy.data.objects['Cube'].select = True
  bpy.ops.object.delete()
  bpy.data.objects['Lamp'].select = True
  bpy.ops.object.delete()

def position_around_origin(obj, distance, deltaDistance, deltaAngle1, deltaAngle2):
  obj.location = [0, 0, 0]
  obj.rotation_euler = [deltaAngle1 * centered_random(), deltaAngle1 * centered_random(), - math.pi / 2 + deltaAngle1 * centered_random()]

  distz = mathutils.Vector((0, 0, distance))
  rotationMAT = obj.rotation_euler.to_matrix()
  rotationMAT.invert()
  zVector = distz * rotationMAT
  obj.location += zVector

  obj.location += mathutils.Vector([centered_random() for _ in range(3)]) * deltaDistance
  obj.rotation_euler.x += centered_random() * deltaAngle2
  obj.rotation_euler.y += centered_random() * deltaAngle2
  obj.rotation_euler.z += centered_random() * deltaAngle2

def move_camera():
  camera = bpy.context.scene.camera
  distance = 2 + 6 * random.random()
  position_around_origin(camera, distance, 1 / distance, math.pi / 6, math.pi / 36)
  bpy.data.cameras['Camera'].lens = 20 + 3 * distance * random.random()

def add_random_lightning():
  dataLamp = bpy.data.lamps.new(name='Lamp', type=random.choice(['POINT', 'SUN', 'HEMI', 'AREA']))
  objLamp = bpy.data.objects.new(name='Lamp', object_data=dataLamp)
  bpy.context.scene.objects.link(objLamp)
  dataLamp.color = [1 - 0.5 * random.random() for _ in range(3)]
  dataLamp.distance = 20
  if (dataLamp.type == 'POINT'):
    dataLamp.energy = 5
  if (dataLamp.type == 'AREA'):
    dataLamp.energy = 0.01
  position_around_origin(objLamp, 2 + 6 * random.random(), 1, math.pi / 4, math.pi / 6)

  if (random.random() < 0.1):
    add_random_lightning()

def set_render_params():
  scene = bpy.data.scenes[0]
  scene.render.image_settings.color_depth = '16'
  scene.render.image_settings.file_format = 'PNG'
  bpy.context.scene.render.resolution_x = 600 + int(200 * centered_random())
  bpy.context.scene.render.resolution_y = 600 + int(200 * centered_random())

def initialize_scene():
  delete_default()
  move_camera()
  add_random_lightning()
  set_render_params()
