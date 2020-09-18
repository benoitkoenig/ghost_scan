dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

npx bulksplash --d="$dir/../data/training/paper_textures/" --a=1000 --w=1200 --q="paper texture"
