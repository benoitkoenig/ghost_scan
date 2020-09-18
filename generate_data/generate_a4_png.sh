dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

ls $dir/../data/training/pdf/*.pdf | rev | cut -d "/" -f 1 | cut -d "." -f 2- | rev | xargs -L1 -I {} pdftoppm -png "$dir/../data/training/pdf/{}.pdf" "$dir/../data/training/png/{}"
