dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

$dir/download_backgrounds/main.sh

$dir/generate_a4_png.sh --training
$dir/regenerate_data.sh --training

$dir/generate_a4_png.sh --validation
$dir/regenerate_data.sh --validation

python3 $dir/remove_corrupt_data.py
