#!/usr/bin/env python3
# Use the Python Imaging Library to do the following to a batch of images:
# Open an image
# Rotate an image (90 degrees clockwise)
# Resize an image (128x128)
# Save an image in a specific format in a separate directory (/opt/icons/) (.jpeg)

from PIL import Image
im = Image.open("img/src/_test.jpg")
print(im.format, im.size, im.mode)
out128 = im.resize((128, 128))
out90 = out128.rotate(90)
out90.save("img/dest/_test.jpeg", "JPEG")
out90.show()