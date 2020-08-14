import png

width = 256
height = 256

imgRGB = [[(255, x, y) for x in range(width)] for y in range(height)] # imgRGB is of shape (height, width, 3)
img = [[item for sublist in row for item in sublist] for row in imgRGB] # img is the same as imgRGB, except it is of shape (height, width * 3)

with open('gradient_map.png', 'wb') as f:
  w = png.Writer(width, height, greyscale=False)
  w.write(f, img)
