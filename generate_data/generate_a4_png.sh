dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ -z $1 ]
then
  folder="$dir/../data/training/"
elif [ $1 == "--validation" ] || [ $1 = "-v" ]
then
  folder="$dir/../data/validation/"
else
  folder="$dir/../data/training/"
fi

ls $folder/pdf/*.pdf | rev | cut -d "/" -f 1 | cut -d "." -f 2- | rev | xargs -L1 -I {} pdftoppm -png "$folder/pdf/{}.pdf" "$folder/png/{}"
