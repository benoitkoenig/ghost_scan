import bpy
import bmesh
import math
import random

def subdivide_document():
  me = bpy.data.objects['Document'].data
  bm = bmesh.new()
  bm.from_mesh(me)
  bmesh.ops.subdivide_edges(bm, edges=bm.edges, cuts=20, use_grid_fill=True)
  bm.to_mesh(me)
  me.update()

def add_collision_modifiers():
  bpy.data.objects['Document'].modifiers.new(name='Collision', type='COLLISION')
  bpy.data.objects['Background'].modifiers.new(name='Collision', type='COLLISION')
  bpy.data.objects['Background'].rotation_euler.x = math.pi # Necessary for normals to be right for collisions

def add_softbody_modifier_on_document():
  modifier = bpy.data.objects['Document'].modifiers.new(name='SoftBody', type='SOFT_BODY')
  modifier.settings.use_goal = False
  modifier.settings.use_self_collision = True
  modifier.settings.bend = 1.

def add_force_fields():
  bpy.ops.object.effector_add(type='WIND')
  bpy.data.objects['Field'].field.strength = 1.5
  bpy.ops.object.effector_add(type='FORCE')
  bpy.data.objects['Field.001'].field.strength = 2
  if (random.random() < 0.5): # Then the force field goes in a corner
    cornerSign1 = 1 if random.random() < 0.5 else -1
    cornerSign2 = 1 if random.random() < 0.5 else -1
    bpy.data.objects['Field.001'].location = [random.uniform(cornerSign1 * 2.5, cornerSign1 * 2), random.uniform(cornerSign2 * 2, cornerSign2 * 1.5), random.uniform(-1, -0.2)]
  else: # Then the force field goes near the center
    bpy.data.objects['Field.001'].location = [random.uniform(-2, 2), random.uniform(-1.5, 1.5), random.uniform(-1, -0.2)]

def move_timeframe():
  for i in range(random.randint(0, 30)):
    bpy.context.scene.frame_set(i)

def add_paper_effect():
  obj_doc = bpy.data.objects['Document']
  subdivide_document()
  add_collision_modifiers()
  add_softbody_modifier_on_document()
  add_force_fields()
  move_timeframe()
