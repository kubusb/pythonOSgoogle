#!/usr/bin/env python3

import os
import sys
from PIL import Image
import re

files = [f for f in os.listdir("supplier-data/images/")]
for image in files:
    image_pattern = r'\w*.tiff'
    if re.match(image_pattern, image):
        im = Image.open("supplier-data/images/" + image)
        print(image)
        newname = image.split(".")
        print(newname)
        out600 = im.resize((600, 400))
        outrgb = out600.convert('RGB')
        outrgb.save("/home/student-02-fe81eaa9523b/supplier-data/images/" + newname[0] + ".jpeg", "JPEG")