dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

$dir/generate_a4_png.sh
echo '[Done] Generating A4-format png files'

blender -b -P $dir/blender/main.py
echo '[Done] Generating printed documents and corresponding printed gradient maps'

python3 $dir/generate_documents_without_background.py
echo '[Done] Generating documents without background'

python3 $dir/generate_document_carto.py
echo '[Done] Generating documents carto points'
