#!/usr/bin/sh

#TODO: use program to write in csv

import csv
import os
from pathlib import Path
from google_images_download import google_images_download

img_src_txt_file = "copy_this_to_csv.txt"
images_to_search = []

response = google_images_download.googleimagesdownload()

with open('resources/input.csv') as csv_input:
        reader = csv.reader(csv_input)
        for row in reader:
            images_to_search.append(row[1])

arguments = {"keywords": ','.join(str(e) for e in images_to_search), "limit": "1", "print_urls": True, "size": "medium", "no_directory": True, "format": "jpg"}
paths = response.download(arguments)

print("Move all files from /downloads to anki media folder")
print("Add " + img_src_txt_file + " contents to csv to import in Anki")

Path(img_src_txt_file).touch()
f = open(img_src_txt_file,"w+")
for file_list in paths[0].items():
    f.write("<img src='" + os.path.basename(file_list[1][0]) + "'/>\n")
f.close()
