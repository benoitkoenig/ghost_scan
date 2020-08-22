import bpy

def save_picture(output_file):
  bpy.context.scene.render.filepath = output_file
  bpy.ops.render.render(write_still = True)
