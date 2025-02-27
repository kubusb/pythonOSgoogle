#! /usr/bin/env python3
import os
import requests
import json

feedback_files_list = os.listdir("/data/feedback")
#print(feedback_files_list)

# Reading each file line into a dict, with keys:
# title
# name
# date
# feedback

feedback_dict = {}
for feedback_file in feedback_files_list:
    with open("/data/feedback/" + feedback_file) as file:
        index_names = ["title", "name", "date", "feedback"]
        index_num = 0
        for line in file:
            feedback_dict[index_names[index_num]] = line.strip()
            index_num += 1
        package = json.dumps(feedback_dict).strip()
        package_verified = json.loads(package)
        response = requests.post("http://34.122.165.35/feedback/", json=package_verified)
        if not response.status_code == 201:
            raise Exception("GET failed with status code {}".format(response.status_code))