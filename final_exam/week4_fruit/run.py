#! /usr/bin/env python3
import os
import requests
import json

supl_data_files_list = os.listdir("supplier-data/descriptions/")
#print(supl_data_files_list)

fruit_dict = {}
for fruit_file in supl_data_files_list:
    with open("supplier-data/descriptions/" + fruit_file) as file:
        index_names = ["name", "weight", "description"]
        index_num = 0
        fruit_dict[["image_name"][index_num]] = fruit_file.split(".")[0] + ".jpeg"
        for line in file:
            if len(line.strip())> 0:
                fruit_dict[index_names[index_num]] = line.strip()
                index_num += 1
        fruit_dict["weight"] = int(fruit_dict["weight"].split(" ")[0])
        package = json.dumps(fruit_dict).strip()
        package_verified = json.loads(package)
        #print(package)
        response = requests.post("http://localhost/fruits/", json=package_verified)
        if not response.status_code == 201:
            raise Exception("GET failed with status code {}".format(response.status_code))
