from PIL import Image

im = Image.open('backgroundcolor.png', 'r')
print(list(im.getdata()))

