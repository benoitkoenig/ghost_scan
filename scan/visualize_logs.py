import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

from ghost_scan.constants import dirpath

if len(sys.argv) != 2:
  print('Usage: python -m scan.visualize_logs [remove_background|detect_pose]')
  exit(1)
filename = sys.argv[1]

with open('%s/scan/logs/%s.csv' % (dirpath, filename)) as csvFile:
  csvReader = csv.reader(csvFile, delimiter=',')
  rows = [r for r in csvReader]
header = rows[0]
rows = rows[1:]
rows = [[float(r) for r in row] for row in rows]
rows = np.array(rows)

fig, ax = plt.subplots(1, 1, figsize=(50, 50))
for i in range(len(rows[0]) - 1):
  ax.plot(rows[:, 0], rows[:, i + 1], label=header[i + 1])
ax.legend()
plt.ylim(-6, 1)
plt.xlim(0, 682)
plt.show()
