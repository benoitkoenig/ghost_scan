dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

blender -b -P $dir/blender/generate_all.py
echo '[Done] Generating printed documents and corresponding printed gradient maps'

python3 $dir/generate_documents_without_background.py
echo '[Done] Generating documents without background'

python3 $dir/generate_document_carto.py
echo '[Done] Generating documents carto points'