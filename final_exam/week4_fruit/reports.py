#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date
import os
import json

def generate_report():
    report = SimpleDocTemplate("/tmp/processed.pdf")
    styles = getSampleStyleSheet()
    today = date.today()

    supl_data_files_list = os.listdir("supplier-data/descriptions/")

    pdf_fruit_dict = {}
    table_data = []
    for fruit_file in supl_data_files_list:
        with open("supplier-data/descriptions/" + fruit_file) as file:
            index_names = ["name", "weight"]
            index_num = 0
            for line in file:
                if index_num < 2:
                    if len(line.strip())> 0:
                        pdf_fruit_dict[index_names[index_num]] = line.strip()
                        index_num += 1
            package = json.dumps(pdf_fruit_dict).strip()
            package_verified = json.loads(package)
            # Unpack this dict to two dimensional array
            for k, v in pdf_fruit_dict.items():
                table_data.append([k, v])

    report_title = Paragraph("Processed Update on " + str(today), styles["h1"])
    report_table = Table(data=table_data)

    report.build([report_title, report_table])

if __name__ == "__main__":
  generate_report()