dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

$dir/download_backgrounds/main.sh

python3 $dir/generate_a4_png/generate_training_png.py
python3 $dir/generate_a4_png/generate_validation_png.py

$dir/regenerate_data.sh --training

$dir/regenerate_data.sh --validation

python3 $dir/remove_corrupt_data.py
