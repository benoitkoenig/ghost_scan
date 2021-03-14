import urllib.request
import requests
import re
from pathlib import Path
import tempfile

dirpath = tempfile.mkdtemp()
a4PdfFilepath = '%s/a4.pdf' % dirpath

def get_pdf_generator():
  page = 0
  filename = Path(a4PdfFilepath)
  while (True):
    contents = urllib.request.urlopen("https://arxiv.org/search/?query=a&searchtype=all&order=-announced_date_first&size=50&abstracts=show&start=%s" % (50 * page)).read().decode('utf-8')
    page += 1
    results = re.findall(r"\"https://arxiv.org/pdf/.+?\"", contents)
    for r in results:
      pdfUrl = "%s.pdf" % r.replace("\"", "")
      response = requests.get(pdfUrl)
      filename.write_bytes(response.content)
      yield a4PdfFilepath
