import csv

from ghost_scan.constants import dirpath
from ghost_scan.generate_data.constants import training_dataset_expected_size

with open('%s/generate_data/download_backgrounds/oidv6-train-images-with-labels-with-rotation.csv' % dirpath) as inputCsvFile:
  with open('%s/generate_data/download_backgrounds/image_list_file.csv' % dirpath, 'w') as outpufCsvFile:
    csvReader = csv.reader(inputCsvFile, delimiter=',')
    csvWriter = csv.writer(outpufCsvFile, delimiter=',')
    i = 0
    for r in csvReader:
      i += 1
      if (i == 1):
        continue # ignore the first row
      csvWriter.writerow(['%s/%s' % (r[1], r[0])])
      if (i == training_dataset_expected_size + 1):
        break
