import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

dirpath = os.path.dirname(__file__)

img1 = mpimg.imread('%s/printed_document.png' % dirpath)
img2 = mpimg.imread('%s/printed_gradient_map.png' % dirpath)

fig, axs = plt.subplots(1, 2, figsize=(50, 50))
axs[0].imshow(img1)
axs[1].imshow(img2)
plt.show()
