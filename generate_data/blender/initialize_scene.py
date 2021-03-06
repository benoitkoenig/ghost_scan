import bpy
import math
import mathutils
import random

def delete_default():
  bpy.ops.wm.read_factory_settings(use_empty=True)

def position_around_origin(obj, distance, deltaDistance, deltaAngle1, deltaAngle2):
  obj.location = [0, 0, 0]
  obj.rotation_euler = [deltaAngle1 * random.uniform(-1, 1), deltaAngle1 * random.uniform(-1, 1), - math.pi / 2 + deltaAngle1 * random.uniform(-1, 1)]

  distz = mathutils.Vector((0, 0, distance))
  rotationMAT = obj.rotation_euler.to_matrix()
  rotationMAT.invert()
  zVector = distz * rotationMAT
  obj.location += zVector

  obj.location += mathutils.Vector([random.uniform(-1, 1) for _ in range(3)]) * deltaDistance
  obj.rotation_euler.x += random.uniform(-1, 1) * deltaAngle2
  obj.rotation_euler.y += random.uniform(-1, 1) * deltaAngle2
  obj.rotation_euler.z += random.uniform(-1, 1) * deltaAngle2

def add_camera():
  dataCamera = bpy.data.cameras.new(name='Camera')
  camera = bpy.data.objects.new(name='Lamp', object_data=dataCamera)
  bpy.context.scene.camera = camera
  distance = 2 + 6 * random.random()
  position_around_origin(camera, distance, 1 / distance, math.pi / 6, math.pi / 36)
  dataCamera.lens = 20 + 3 * distance * random.random()

def add_lamps():
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
    add_lamps()

def set_render_params():
  scene = bpy.data.scenes[0]
  scene.render.image_settings.color_depth = '16'
  scene.render.image_settings.file_format = 'PNG'
  bpy.context.scene.render.resolution_x = 600 + int(200 * random.uniform(-1, 1))
  bpy.context.scene.render.resolution_y = 600 + int(200 * random.uniform(-1, 1))

def initialize_scene():
  delete_default()
  add_camera()
  add_lamps()
  set_render_params()
