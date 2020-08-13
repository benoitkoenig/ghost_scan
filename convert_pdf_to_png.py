import os

os.system('mkdir ./tmp') # For some reason, "mktemp -d" does not help

pdfFiles = [pdfFile for pdfFile in os.listdir('./data/pdf/') if pdfFile[-4:] == '.pdf']

for pdfFile in pdfFiles:
  os.system('pdftk "./data/pdf/%s" burst output ./tmp/pg_%s.pdf' % (pdfFile, '%04d'))
  os.system('ls ./tmp/pg*.pdf | xargs -L1 -I {} inkscape {} -z --export-dpi=300 --export-area-drawing --export-png="{}-%s.png"' % pdfFile)
  os.system('mv ./tmp/*.png ./data/png/')
  os.system('rm ./tmp/*')
  os.system('rm "./data/pdf/%s"' % pdfFile)

os.system('rmdir ./tmp')
