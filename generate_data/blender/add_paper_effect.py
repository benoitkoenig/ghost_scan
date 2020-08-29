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
  bpy.data.objects['Field'].field.strength = 2.2
  bpy.ops.object.effector_add(type='TURBULENCE')
  bpy.data.objects['Field.001'].field.strength = 0.5

def move_timeframe():
  for i in range(random.randint(0, 50)):
    bpy.context.scene.frame_set(i)

def add_paper_effect():
  obj_doc = bpy.data.objects['Document']
  subdivide_document()
  add_collision_modifiers()
  add_softbody_modifier_on_document()
  add_force_fields()
  move_timeframe()
