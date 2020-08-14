ls ./data/png/*.png | cut -d '/' -f 4 | xargs -L1 -I {} blender -b -P generate_single_picture.py -- {}
