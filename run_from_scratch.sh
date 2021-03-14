./install.sh
./generate_data/main.sh
python3 -m scan.remove_background.train
python3 -m scan.detect_pose.train
