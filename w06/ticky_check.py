#!/usr/bin/env python3

import operator
import re
import os
import csv

error = {}
per_user = {}
unique_users = []
per_user_infos = {}
per_user_errors = {}
final_resultf1 = []
final_resultf2 = []
final_resultf3 = []

log_file = "syslog.log"
with open(log_file, mode='r',encoding='UTF-8') as file:
    for line in file:
        search_result = re.search(r".*ticky: (ERROR|INFO) (.*) .*\((.*)\)", line.strip())
        if search_result is not None:
            if search_result.group(3) not in unique_users:
                unique_users.append(search_result.group(3))
            if search_result.group(1) == "ERROR":
                error[search_result.group(2)] = error.get(search_result.group(2), 0) +1
                #per_user_errors[search_result.group(3)] = per_user_errors.get(search_result.group(3), 0) +1
                
            #if search_result.group(1) == "INFO":
                #per_user_infos[search_result.group(3)] = per_user_infos.get(search_result.group(3), 0) +1

            for name in unique_users:
                if name not in per_user_infos:
                    per_user_infos[name] = 0
                if name not in per_user_errors:
                    per_user_errors[name] = 0
                if search_result.group(3) == name:
                    if search_result.group(1) == "ERROR":
                        per_user_errors[search_result.group(3)] = per_user_errors.get(search_result.group(3), 0) +1
                    elif search_result.group(1) == "INFO":
                        per_user_infos[search_result.group(3)] = per_user_infos.get(search_result.group(3), 0) +1
                
error_sorted = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
per_user_errors_sorted = sorted(per_user_errors.items(), key = operator.itemgetter(0))
per_user_infos_sorted = sorted(per_user_infos.items(), key = operator.itemgetter(0))

for entry in per_user_infos_sorted:
    final_resultf1.append(entry[0])

for entry in per_user_infos_sorted:
    final_resultf2.append(entry[1])

for entry in per_user_errors_sorted:
    final_resultf3.append(entry[1])

rows = zip(final_resultf1, final_resultf2, final_resultf3)

#print("{},{}".format(final_resultf1, final_resultf2))

# Let's write error data to file
error_csv_file = './error_message.csv'

with open(error_csv_file, 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = ["Error", "Count"])
    writer.writeheader()
    writer = csv.writer(csv_file)
    writer.writerows(error_sorted)

# Let's write user data to file
error_csv_file = './user_statistics.csv'

with open(error_csv_file, 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = ["Username", "INFO", "ERROR"])
    writer.writeheader()
    writer = csv.writer(csv_file)
    for row in rows:
        writer.writerow(row)