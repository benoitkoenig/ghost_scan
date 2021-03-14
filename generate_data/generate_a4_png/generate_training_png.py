from ghost_scan.constants import dirpath
from ghost_scan.generate_data.generate_a4_png.pdf_generator import get_pdf_generator
from ghost_scan.generate_data.generate_a4_png.create_a4_png_from_pdf import create_a4_png_from_pdf

limit = 10

def generate_training_png():
  count_a4_png = 0
  gen = get_pdf_generator()
  while count_a4_png < limit:
    pdf_file = next(gen)
    files_added = create_a4_png_from_pdf(pdf_file, "%s/data/training/png" % dirpath, count_a4_png)
    count_a4_png += files_added

generate_training_png()
