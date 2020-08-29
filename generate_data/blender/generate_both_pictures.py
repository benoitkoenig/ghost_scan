import bpy
import bmesh
import math
import random
import sys

from .add_paper_effect import add_paper_effect
from .create_mesh import create_document, create_background
from .initialize_scene import initialize_scene
from .prepare_gradient_picture import prepare_gradient_picture
from .save_picture import save_picture

def generate_both_pictures(inputPath, outputDocumentPath, outputGradientPath):
  initialize_scene()
  create_document(inputPath)
  create_background()
  add_paper_effect()

  save_picture(outputDocumentPath)

  prepare_gradient_picture()
  save_picture(outputGradientPath)
