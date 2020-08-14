import bpy
import bmesh
import math
import random
import sys

def centered_random():
  return 2 * random.random() - 1

def delete_default_cube():
  bpy.data.objects['Cube'].select = True
  bpy.ops.object.delete()

def save_picture(output_file):
  bpy.context.scene.render.filepath = output_file
  bpy.ops.render.render(write_still = True)

def set_lighting_conditions_for_gradient_picture():
  bpy.data.lamps[0].energy = 0

  world = bpy.data.worlds['World']
  world.ambient_color = 0, 0, 0
  world.horizon_color = 0, 0, 0
  world.zenith_color = 0, 0, 0

  mat = bpy.data.materials.get("Material")
  mat.emit = 1
  mat.ambient = 0
  mat.translucency = 0

def add_document_mesh():
  verts = [(0, 0, 0), (0, 2.1, 0), (2.97, 2.1, 0), (2.97, 0, 0)]
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
  bm.free()  # always do this when finished

def set_uv():
  obj = bpy.data.objects['MyObject']
  obj.select = True  # select object
  bpy.ops.object.mode_set(mode='EDIT')
  bpy.ops.mesh.select_mode(type="VERT")
  bpy.ops.mesh.select_all(action = 'SELECT')
  bpy.ops.uv.unwrap()
  bpy.ops.object.mode_set(mode='OBJECT')

def add_texture():
  obj = bpy.data.objects['MyObject']
  mat = bpy.data.materials.get("Material")
  mat.diffuse_intensity = 1
  mat.specular_intensity = 0
  obj.data.materials.append(mat)
  tex = bpy.data.textures.new('Texture', 'IMAGE')
  slot = mat.texture_slots.add()
  slot.texture = tex

def set_texture_image(texture_file):
  bpy.data.textures['Texture'].image = bpy.data.images.load(texture_file)

def move_camera():
  scene = bpy.context.scene
  scene.camera.rotation_mode = 'XYZ'

  scene.camera.location.x = 1.485 + centered_random() / 10
  scene.camera.location.y = 1.05 + centered_random() / 10
  scene.camera.location.z = 10 + centered_random()

  scene.camera.rotation_euler[0] = centered_random() * math.pi / 36
  scene.camera.rotation_euler[1] = centered_random() * math.pi / 36
  scene.camera.rotation_euler[2] = centered_random() * math.pi

def initialize_scene():
  delete_default_cube()
  move_camera()
  add_document_mesh()
  set_uv()
  add_texture()

def main():
  filename = sys.argv[5]
  folderPath = sys.argv[6]

  initialize_scene()

  set_texture_image('%s/data/png/%s' % (folderPath, filename))
  save_picture('%s/data/printed_document/%s' % (folderPath, filename))

  set_lighting_conditions_for_gradient_picture()
  set_texture_image('%s/generate_data/gradient_map.png' % folderPath)
  save_picture('%s/data/printed_gradient_map/%s' % (folderPath, filename))

main()
