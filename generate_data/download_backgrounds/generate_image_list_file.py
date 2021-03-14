import csv

from ghost_scan.constants import dirpath

limit = 5000

with open('%s/generate_data/download_background_pictures/oidv6-train-images-with-labels-with-rotation.csv' % dirpath) as inputCsvFile:
  with open('%s/generate_data/download_background_pictures/image_list_file.csv' % dirpath, 'w') as outpufCsvFile:
    csvReader = csv.reader(inputCsvFile, delimiter=',')
    csvWriter = csv.writer(outpufCsvFile, delimiter=',')
    i = 0
    for r in csvReader:
      i += 1
      if (i == limit):
        break
      csvWriter.writerow(['train/%s' % r[0]])
