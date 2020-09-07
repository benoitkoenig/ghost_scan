read -p "Did you already load data/pdf/ with a4-format pdf files? [y/N] " yn
case $yn in
  [Yy] ) ;;
  * ) exit;;
esac

./install.sh
./generate_data/download_backgrounds.sh
./generate_data/download_paper_textures.sh
./generate_data/generate_a4_png.sh
./generate_data/regenerate_data.sh
python3 -m scan.remove_background.train
python3 -m scan.get_carto_by_points.train
