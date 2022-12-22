#!/usr/bin/env python3
import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, mode='w') as text_file:
    text_file.write(comments)
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))
# check = open("program.py", "r")
# print(check.readlines())
# check.close()