#!/usr/bin/env python

from tempfile import NamedTemporaryFile
import shutil
import csv
import gspread
import getpass


def pull_gspread():

    # Get Google Drive credentials
    username = raw_input('Drive Username: ')
    password = getpass.getpass(prompt='Drive Password: ')
    filename = raw_input('Drive Filename: ')
    column_number = raw_input('Total Grade Column Number: ')

    # Log in
    print "Logging into Google Drive"
    gc = gspread.login(username, password)

    # Open sheet
    wks = gc.open(filename).sheet1

    # Download
    print "Downloading Data Ranges..."
    return wks.col_values(int(column_number))


def edit_csv(grades):

    print "Editing CSV"
    filename = 'grades.csv'
    tempfile = NamedTemporaryFile(delete=False)

    with open(filename, 'rb') as csvFile, tempfile:
        reader = csv.reader(csvFile)
        writer = csv.writer(tempfile)

        count = 0
        while count < 3:
            row = reader.next()
            writer.writerow(row)
            count = count + 1

        i = 1
        for row in reader:
            row[4] = float(grades[i])
            writer.writerow(row)
            i = i + 1

    shutil.move(tempfile.name, filename)


def main():
    grade_data = pull_gspread()
    edit_csv(grade_data)

if __name__ == '__main__':
    main()
