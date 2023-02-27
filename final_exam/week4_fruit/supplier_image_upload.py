#!/usr/bin/env python3
import requests
import os
import re

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

files = [f for f in os.listdir("supplier-data/images/")]
for image in files:
    image_pattern = r'\w*.jpeg'
    if re.match(image_pattern, image):
        with open('supplier-data/images/' + image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})


