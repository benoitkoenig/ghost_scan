import csv

coords = [(0, 0), (0, 1), (1, 0), (1, 1)]
numberOfPoints = len(coords)

with open('data/printed_document_carto.csv') as csvFile:
  csvReader = csv.reader(csvFile, delimiter=',')
  rows = [0 for r in csvReader][1:]
filesCount = len(rows)
