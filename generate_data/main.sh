dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

$dir/generate_a4_png.sh
echo '[Done] Generating A4-format png files'

ls $dir/../data/png/*.png | rev | cut -d '/' -f 1 | rev | xargs -L1 -I {} blender -b -P $dir/generate_single_picture.py -- {} "$dir/.."
echo '[Done] Generating printed documents and corresponding printed gradient maps'

python3 $dir/generate_documents_without_background.py
echo '[Done] Generating documents without background'

python3 $dir/generate_document_cartography.py
echo '[Done] Generating documents cartography points'