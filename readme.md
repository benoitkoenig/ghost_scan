# Usage

## Data generation
- To generate the data from pdf documents in data/pdf: `./generate_data/generate_data_from_pdf.sh`
- To check the data generation on a single example: `./generate_data/check/check.sh`

## Get gradient map model
- To train the model: `python -m get_gradient_map_from_printed_document.train.py`
- To visualize a single prediction: `python -m ghost_scan.get_gradient_map_from_printed_document.visualize_prediction {filename}.png`

## Get document cartography model
- To train the model: `python -m get_cartography_from_printed_document.train.py`
- To visualize a single prediction: `python -m ghost_scan.get_cartography_from_printed_document.visualize_prediction {filename}.png`
