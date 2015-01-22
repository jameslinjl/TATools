#!/bin/bash
# requires the download_grade_zip python source

# remove old zip to ensure correct naming
rm bulk_download.zip &> /dev/null

# download the zip file to current folder
echo 'starting download script'
python download_grade_zip.py
echo 'finished download'

# stall while file is not present
while [ ! -f bulk_download.zip ]
do
    sleep 1
done

# unzip the new download
unzip bulk_download.zip

# cd into homework directory
cd Homework*

# move grades.csv into previous directory
mv grades.csv ..

# pull grades from correct spreadsheet
echo 'pulling grades from google spreadsheet'
# update the csv
# zip all the stuff up
# selenium script to upload

# add option saying which homework
