mkdir ./tmp # For some reason, "mktemp -d" does not help
ls ./data/pdf/*.pdf | cut -d "/" -f 4 | xargs -L1 -I {} pdftk "./data/pdf/{}" burst output ./tmp/{}-pg_%04d.pdf
ls ./tmp/*.pdf | xargs -L1 -I {} inkscape {} -z --export-dpi=300 --export-area-drawing --export-png="{}.png"
ls ./tmp/*.png | xargs -L1 -I {} convert {} -rotate 90 {}
mv ./tmp/*.png ./data/png/
rm ./data/pdf/*.pdf
rm -r ./tmp
