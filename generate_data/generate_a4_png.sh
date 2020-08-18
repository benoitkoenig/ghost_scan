dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

tmp=$(mktemp -d)
ls $dir/../data/pdf/*.pdf | rev | cut -d "/" -f 1 | cut -d "." -f 2- | rev | xargs -L1 -I {} pdftoppm -png "$dir/../data/pdf/{}.pdf" "$tmp/{}"
ls $tmp/*.png | xargs -L1 -I {} convert {} -rotate 90 {}
mv $tmp/*.png $dir/../data/png/
