#!/usr/bin/env python3
import psutil
import socket

# Calling psutil.cpu_precent() for 5 seconds
cpu_usage_5 = psutil.cpu_percent(5)
if cpu_usage_5 > 80:
    print('The CPU usage is: ', cpu_usage_5)
else:
    print("nothing is wrong with the CPU")

# Show free memory
free_virtual_memory = psutil.virtual_memory().free
if free_virtual_memory < (500 * 1024 * 1024):
    print('The free mem in MB is: ', free_virtual_memory / 1024 / 1024)
else:
    print('Nothing is wrong with the RAM')

# Show disk udage
used_disk_space_percent = psutil.disk_usage('/').percent
if used_disk_space_percent > 80:
    print('The used diskspace percent is: ', used_disk_space_percent)
else:
    print('Nothing is wrong with the disk')

# Host resolution
socket_local = socket.gethostbyname('localhost')
if socket_local == '127.0.0.1':
    print('Network OK:', socket_local)
else:
    print('Network failed')