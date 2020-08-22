import os

from ghost_scan.generate_data.generate_blender_pictures.initialize_scene import initialize_scene
from ghost_scan.generate_data.generate_blender_pictures.create_document import create_document, set_texture_image
from ghost_scan.generate_data.generate_blender_pictures.prepare_gradient_picture import prepare_gradient_picture
from ghost_scan.generate_data.generate_blender_pictures.save_picture import save_picture

dirpath = os.path.dirname(__file__)

initialize_scene()
create_document()

set_texture_image('%s/input.png' % dirpath)
save_picture('%s/printed_document.png' % dirpath)

prepare_gradient_picture()
set_texture_image('%s/../../gradient_map.png' % dirpath)
save_picture('%s/printed_gradient_map.png' % dirpath)
