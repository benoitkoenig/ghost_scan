import os

from ghost_scan.generate_data.generate_blender_pictures.main import initialize_scene, set_texture_image, save_picture, set_lighting_conditions_for_gradient_picture

dirpath = os.path.dirname(__file__)

initialize_scene()

set_texture_image('%s/input.png' % dirpath)
save_picture('%s/printed_document.png' % dirpath)

set_lighting_conditions_for_gradient_picture()
set_texture_image('%s/../gradient_map.png' % dirpath)
save_picture('%s/printed_gradient_map.png' % dirpath)
