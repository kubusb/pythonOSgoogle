#!/usr/bin/env python3
# Use the Python Imaging Library to do the following to a batch of images:
# Open an image
# Rotate an image (90 degrees clockwise)
# Resize an image (128x128)
# Save an image in a specific format in a separate directory (/opt/icons/) (.jpeg)
import os
import sys
from PIL import Image

files = [f for f in os.listdir("img/src/")]
for image in files:
    im = Image.open("img/src/" + image)
    print(image)
    out128 = im.resize((128, 128))
    out90 = out128.rotate(90)
    outrgb = out90.convert('RGB')
    outrgb.save("img/dest/" + image, "JPEG")