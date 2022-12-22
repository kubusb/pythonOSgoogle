#!/usr/bin/env python3mod 700 file  
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open (filename, "w") as file:
    pass
  timestamp = os.stat(filename).st_mtime
  # Convert the timestamp into a readable format, then into a string
  human_timestamp = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(str(human_timestamp)[:10]))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd