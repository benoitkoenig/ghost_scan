set -e

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
blender -b -P $dir/generate.py
python3 $dir/visualize.py
