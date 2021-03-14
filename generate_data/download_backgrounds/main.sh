dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ ! -f $dir/downloader.py ]; then
  wget https://raw.githubusercontent.com/openimages/dataset/master/downloader.py -O $dir/downloader.py
fi
if [ ! -f $dir/oidv6-train-images-with-labels-with-rotation.csv ]; then
  wget https://storage.googleapis.com/openimages/v6/oidv6-train-images-with-labels-with-rotation.csv -O $dir/oidv6-train-images-with-labels-with-rotation.csv
fi

python3 $dir/generate_image_list_file.py

python3 $dir/downloader.py $dir/image_list_file.csv --download_folder=$dir/../../data/training/backgrounds --num_processes=5
