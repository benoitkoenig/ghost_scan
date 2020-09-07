dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

$dir/download_backgrounds.sh
$dir/download_paper_textures.sh
$dir/generate_a4_png.sh
$dir/regenerate_data.sh
