# GhostScan

GhostScan is a project to scan a document with the best quality possible from a picture

## Installation

Use `install.sh`

## Data generation
To generate data, you need pdf files and background images. You need to manually add pdf files (a4 format for all pages) in the folder data/pdf. As for backgrounds and paper textures, you can download them from unsplash.com using respectively `generate_data/download_backgrounds.sh` and `generate_data/download_paper_textures.sh`. Once this is done, you can simply run `generate_data/main.sh` and let the script do the rest<br />
In case you want to edit blender's files generations, you can check your script with `generate_data/blender/check/main.sh`

## Training models

You can train all models by doing `python -m scan.{folder_name}.train` and visualize the result with `python -m scan.{folder_name}.check {filename.png}`
Currently, only two models are used: `remove_background` and `get_carto_by_points`.<br />`get_carto_by_gradient` does a similar job as `get_carto_by_points`, though the latter currently yields better results

## Scan an image

To actually scan an image, you can use the function "scan" defined in `scan/scan.py`, that takes as input the image data (an array to be converted to numpy array)
To check the whole scanning process, you can use `python -m scan.check [-v|--validation] {filename.png|jpg}`. You will then be prompted with the filenames you want to check. Use "-v" to pick images in "data/validation_data/printed_document" instead of "data/printed_document"
