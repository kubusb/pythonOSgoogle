#!/usr/bin/env python3
import psutil
import socket
import emails

# Sending e-mails
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = ""
body = "Please check your system and resolve the issue as soon as possible." 

# Calling psutil.cpu_precent() for 5 seconds
cpu_usage_5 = psutil.cpu_percent(5)
if cpu_usage_5 > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)
else:
    print("nothing is wrong with the CPU")

# Show free memory
free_virtual_memory = psutil.virtual_memory().free
if free_virtual_memory < (500 * 1024 * 1024):
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)
else:
    print('Nothing is wrong with the RAM')

# Show disk udage
used_disk_space_percent = psutil.disk_usage('/').percent
if used_disk_space_percent > 80:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)
else:
    print('Nothing is wrong with the disk')

# Host resolution
socket_local = socket.gethostbyname('localhost')
if socket_local == '127.0.0.1':
    print('Network OK:', socket_local)
else:
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)