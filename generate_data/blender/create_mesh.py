import bpy
import bmesh
import os
import random
import sys

from ghost_scan.constants import dirpath

if ('-v' in sys.argv) | ('--validation' in sys.argv):
  folderpath = '%s/data/validation' % dirpath
else:
  folderpath = '%s/data/training' % dirpath

backgrounds_filepaths = ['%s/backgrounds/%s' % (folderpath, f) for f in os.listdir('%s/backgrounds/' % folderpath) if (f[-4:] == '.jpg')]
paper_textures_filepaths = ['%s/paper_textures/%s' % (folderpath, f) for f in os.listdir('%s/paper_textures/' % folderpath) if (f[-4:] == '.jpg')]

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

def add_material(name):
  obj = bpy.data.objects[name]
  bpy.ops.object.shade_smooth()
  mat = bpy.data.materials.new(name='Mat%s' % name)
  mat.diffuse_intensity = 1
  mat.specular_intensity = 0.1 * random.random()
  mat.specular_hardness = 50 * random.random()
  obj.data.materials.append(mat)

def add_object(name, verts):
  add_mesh(name, verts)
  add_material(name)
  set_uv(name)

def add_texture(name, texture_name, texture_file, apply_random_factor=False, only_normal=False):
  mat = bpy.data.materials['Mat%s' % name]
  tex = bpy.data.textures.new('Texture%s%s' % (name, texture_name), 'IMAGE')

  if (apply_random_factor):
    tex.factor_red = (1 - random.random() ** 2)
    tex.factor_green = (1 - random.random() ** 2)
    tex.factor_blue = (1 - random.random() ** 2)
  slot = mat.texture_slots.add()
  slot.texture = tex
  if (only_normal):
    slot.use_map_color_diffuse = False
    slot.use_map_normal = True
    slot.normal_factor = random.random()
  tex.image = bpy.data.images.load(texture_file)

def create_document(filepath):
  add_object('Document', [(-1.485, -1.05, 0.01), (-1.485, 1.05, 0.01), (1.485, 1.05, 0.01), (1.485, -1.05, 0.01)])
  add_texture('Document', 'Page', filepath, apply_random_factor=True)
  add_texture('Document', 'Paper', random.choice(paper_textures_filepaths), only_normal=True)

def create_background():
  add_object('Background', [(-5, -5, 0), (-5, 5, 0), (5, 5, 0), (5, -5, 0)])
  add_texture('Background', 'Background', random.choice(backgrounds_filepaths))
  bpy.data.materials.get('MatBackground').emit = 0.2 * random.random() # To avoid shadows being all-black
