import bpy
import bmesh

def delete_default_cube():
  bpy.data.objects['Cube'].select = True
  bpy.ops.object.delete()

def save_picture():
  bpy.context.scene.render.filepath = './image.png'
  bpy.ops.render.render(write_still = True)

def add_document_mesh():
  verts = [(0, 0, 0), (0, 2.1, 0), (2.97, 2.1, 0), (2.97, 0, 0)]
  mesh = bpy.data.meshes.new('mesh')  # add a new mesh
  obj = bpy.data.objects.new('MyObject', mesh)  # add a new object using the mesh

  scene = bpy.context.scene
  scene.objects.link(obj)  # put the object into the scene (link)
  scene.objects.active = obj  # set as the active object in the scene
  obj.select = True  # select object

  mesh = bpy.context.object.data
  bm = bmesh.new()

  vertices = [bm.verts.new(v) for v in verts]
  bm.faces.new(vertices)

  # make the bmesh the object's mesh
  bm.to_mesh(mesh)  
  bm.free()  # always do this when finished

delete_default_cube()
add_document_mesh()
save_picture()
