from ghost_scan.constants import dirpath
from ghost_scan.generate_data.generate_a4_png.create_a4_png_from_pdf import create_a4_png_from_pdf

def generate_validation_png():
  pdf_file = '%s/data/validation/pdf/rapport.pdf' % dirpath
  create_a4_png_from_pdf(pdf_file, "%s/data/validation/png" % dirpath, 'rapport')

generate_validation_png()
