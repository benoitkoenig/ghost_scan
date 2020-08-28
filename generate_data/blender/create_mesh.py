import bpy
import bmesh
import os
import random

def add_mesh(name, verts):
  mesh = bpy.data.meshes.new('mesh')  # add a new mesh
  obj = bpy.data.objects.new(name, mesh)  # add a new object using the mesh

  scene = bpy.context.scene
  scene.objects.link(obj)  # put the object into the scene (link)
  scene.objects.active = obj  # set as the active object in the scene
  obj.select = True  # select object

  mesh = obj.data
  bm = bmesh.new()

  vertices = [bm.verts.new(v) for v in verts]
  bm.faces.new(vertices)

  # make the bmesh the object's mesh
  bm.to_mesh(mesh)
  bm.free() # always do this when finished

def set_uv(name):
  obj = bpy.data.objects[name]
  obj.select = True  # select object
  bpy.ops.object.mode_set(mode='EDIT')
  bpy.ops.mesh.select_mode(type='VERT')
  bpy.ops.mesh.select_all(action = 'SELECT')
  bpy.ops.uv.unwrap()
  bpy.ops.object.mode_set(mode='OBJECT')

  uv_layer = obj.data.uv_layers.active
  uv_layer.data[0].uv = [1, 0]
  uv_layer.data[1].uv = [0, 0]
  uv_layer.data[2].uv = [0, 1]
  uv_layer.data[3].uv = [1, 1]

def add_texture(name):
  obj = bpy.data.objects[name]
  mat = bpy.data.materials.new(name='Mat%s' % name)
  mat.diffuse_intensity = 1
  mat.specular_intensity = 0.1 * random.random()
  mat.specular_hardness = 50 * random.random()
  obj.data.materials.append(mat)
  tex = bpy.data.textures.new('Texture%s' % name, 'IMAGE')

  tex.factor_red = (1 - random.random() ** 2)
  tex.factor_green = (1 - random.random() ** 2)
  tex.factor_blue = (1 - random.random() ** 2)
  slot = mat.texture_slots.add()
  slot.texture = tex

def set_texture_image(name, texture_file):
  bpy.data.textures['Texture%s' % name].image = bpy.data.images.load(texture_file)

def create_document(filepath):
  z = 0.01 + random.random()
  add_mesh('Document', [(-1.485, -1.05, z), (-1.485, 1.05, z), (1.485, 1.05, z), (1.485, -1.05, z)])
  set_uv('Document')
  add_texture('Document')
  set_texture_image('Document', filepath)

def create_background():
  add_mesh('Background', [(-5, -5, 0), (-5, 5, 0), (5, 5, 0), (5, -5, 0)])
  set_uv('Background')
  add_texture('Background')
  bpy.data.materials.get('MatBackground').emit = 0.2 * random.random() # To avoid shadows being all-black

  dirname = os.path.dirname(__file__)
  filename = random.choice([f for f in os.listdir('%s/../../data/backgrounds/' % dirname) if (f[-4:] == '.jpg')])
  set_texture_image('Background', '%s/../../data/backgrounds/%s' % (dirname, filename))
