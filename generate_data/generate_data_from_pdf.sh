dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# First step: generate A4-format png pictures from pdf
mkdir ./tmp # For some reason, "mktemp -d" does not help
ls $dir/../data/pdf/*.pdf | rev | cut -d "/" -f 1 | rev | xargs -L1 -I {} pdftk "$dir/../data/pdf/{}" burst output ./tmp/{}-pg_%04d.pdf
ls ./tmp/*.pdf | xargs -L1 -I {} inkscape {} -z --export-dpi=300 --export-area-drawing --export-png="{}.png"
ls ./tmp/*.png | xargs -L1 -I {} convert {} -rotate 90 {}
mv ./tmp/*.png ./data/png/
rm -r ./tmp

# Second: generate pictures of printed documents, as well as the exact same picture of the gradient
ls $dir/../data/png/*.png | rev | cut -d '/' -f 1 | rev | xargs -L1 -I {} blender -b -P $dir/generate_single_picture.py -- {} "$dir/.."

# Third, generate the printed document without its background
python3 $dir/generate_documents_without_background.py

# Fourth, generate the cartography document, as a csv
python3 $dir/generate_document_cartography.py
