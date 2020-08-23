import bpy
import bmesh
import mathutils

def add_document_mesh():
  verts = [(-1.485, -1.05, 0), (-1.485, 1.05, 0), (1.485, 1.05, 0), (1.485, -1.05, 0)]
  mesh = bpy.data.meshes.new('mesh')  # add a new mesh
  obj = bpy.data.objects.new('MyObject', mesh)  # add a new object using the mesh

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

def set_uv():
  obj = bpy.data.objects['MyObject']
  obj.select = True  # select object
  bpy.ops.object.mode_set(mode='EDIT')
  bpy.ops.mesh.select_mode(type='VERT')
  bpy.ops.mesh.select_all(action = 'SELECT')
  bpy.ops.uv.unwrap()
  bpy.ops.object.mode_set(mode='OBJECT')

  obj.data.uv_layers.active.data[0].uv = mathutils.Vector([1, 0])
  obj.data.uv_layers.active.data[1].uv = mathutils.Vector([0, 0])
  obj.data.uv_layers.active.data[2].uv = mathutils.Vector([0, 1])
  obj.data.uv_layers.active.data[3].uv = mathutils.Vector([1, 1])

def add_texture():
  obj = bpy.data.objects['MyObject']
  mat = bpy.data.materials.get('Material')
  mat.diffuse_intensity = 1
  mat.specular_intensity = 0
  obj.data.materials.append(mat)
  tex = bpy.data.textures.new('Texture', 'IMAGE')
  slot = mat.texture_slots.add()
  slot.texture = tex

def set_texture_image(texture_file):
  bpy.data.textures['Texture'].image = bpy.data.images.load(texture_file)

def create_document():
  add_document_mesh()
  set_uv()
  add_texture()
