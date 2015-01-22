#!/bin/bash
# requires the download_grade_zip python source to be in same directory
# requires the csv_script python source to be in same directory
# requires gspread python module

# remove old zip to ensure correct naming
rm bulk_download.zip &> /dev/null

# download the zip file to current folder
echo 'starting download script'
python selenium_script.py 1
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
cd ..

# pull grades from correct spreadsheet
# update the csv
echo 'pulling grades from google spreadsheet'
python csv_script.py

# optional to have comments updated and send grade reports
# python sheet_to_comments.py
# python mailscript.py

# zip all the stuff up
mv grades.csv Homework*
rm upload.zip &> /dev/null
zip -r upload Homework*

# selenium script to upload
python selenium_script.py 2

# clean up
rm upload.zip &> /dev/null
rm bulk_download.zip &> /dev/null