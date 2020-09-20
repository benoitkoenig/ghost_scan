read -p "Did you already load data/pdf/ with a4-format pdf files? [y/N] " yn
case $yn in
  [Yy] ) ;;
  * ) exit;;
esac

./install.sh
./generate_data/main.sh
python3 -m scan.remove_background.train
python3 -m scan.detect_pose.train
