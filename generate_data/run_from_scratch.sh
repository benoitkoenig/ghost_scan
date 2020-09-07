echo 'Make sure you already have many a4-format pdfs in data/pdf/, as those are not automatically fetched anywhere for now'
./download_backgrounds.sh
./download_paper_textures.sh
./generate_a4_png.sh
./regenerate_data.sh
