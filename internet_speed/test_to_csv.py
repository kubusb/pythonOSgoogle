#!/usr/local/bin/python3
from datetime import datetime
import subprocess
import json
import os
import csv

def write_int_speed_to_csv():
    # datetime object containing current date and time
    now = datetime.now()
    
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y-%m-%d %H:%M")

    # Let's measure the internet speed
    pomiar = subprocess.run(["/usr/local/bin/fast", "-u", "--single-line", "--json"], capture_output=True, text=False)

    # grab the result and decode it
    data = json.loads(pomiar.stdout.decode())

    pomiar_download = data["downloadSpeed"]
    pomiar_upload = data["uploadSpeed"]
    pomiar_ping = data["latency"]

    csv_row = [dt_string, pomiar_download, pomiar_upload, pomiar_ping]

    # Let's write this data to file
    csv_file = '/home/pi/repositories/pythonOSgoogle/internet_speed/speedtest.csv'
    isFile = os.path.isfile(csv_file)

    if isFile:
        with open(csv_file, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(csv_row)
    else:
        with open(csv_file, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["date_time", "dl_speed", "ul_speed", "ping"])
            writer.writeheader()
            writer = csv.writer(csv_file)
            writer.writerow(csv_row)

write_int_speed_to_csv()
