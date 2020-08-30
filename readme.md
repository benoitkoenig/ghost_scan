# GhostScan

GhostScan is a project to scan a document with the best quality possible from a picture

## Installation

Use `install.sh`

## Data generation
To generate data, you need pdf files and background images. You need to manually add pdf files (a4 format for all pages) in the folder data/pdf. As for backgrounds, you can download them from unsplash.com using the script `generate_data/download_backgrounds.sh`. Once this is done, you can simply run `generate_data/main.sh` and let the script do the rest<br />
In case you want to edit blender's files generations, you can check your script with `generate_data/blender/check/check.sh`

## Training models

You can train all models by doing `python -m scan.{folder_name}.train` and visualize the result with `python -m scan.{folder_name}.visualize {filename.png}`
Currently, only two models are used: `remove_background` and `get_carto_by_points`.<br />`get_carto_by_gradient` is hopefully expected to take `get_carto_by_points` role at some point, but currently does not yield good enough results

## Scan an image

To scan an image from the training set with your trained models, use `python -m scan.scan {filename.png}`<br />
To actually scan an image outside of the training set, put it in `data/validation_data/printed_document/` and run `python -m scan.scan -v {filename.png|jpg}`
