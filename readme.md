# GhostScan

GhostScan is a project to scan a document with the best quality possible from a picture

# Data generation
- To generate the data from pdf documents in data/pdf: `./generate_data/main.sh`
- To check the data generation on a single example: `./generate_data/check_blender/check.sh`

# Running and testing deep learning models

## Remove the background

Removing the background is done by segmentation
- Training: `python -m get_gradient_map_from_printed_document.train.py`
- Checking: `python -m ghost_scan.get_gradient_map_from_printed_document.visualize_prediction {filename}.png`

## Get cartography by gradient

Getting cartography by creating the printed gradient map from the printed document
- Training: `python -m get_cartography_by_gradient.train.py`
- Checking: `python -m get_cartography_by_gradient.visualize_prediction {filename}.png`

## Get cartography by points

Getting cartography by estimating the positions of pre-defined coordinates
- Training: `python -m get_cartography_by_points.train.py`
- Checking: `python -m get_cartography_by_points.visualize_prediction {filename}.png`
