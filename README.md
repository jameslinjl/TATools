This repo is for little useful tools and scripts for doing TA stuff.

<b>sheet_to_comments.py</b>

Uses gspread (Google Spreadsheets Python API - https://github.com/burnash/gspread)

This is a short Python script which interacts with a Google Spreadsheet. After getting
your username and password, the script will go through each provided cell and transfer
the information to a .txt file which can be directly uploaded to Columbia University's
Courseworks comment section. The script is to be run from the same level as the 
downloaded batch homework folder.

<b>mailscript.py</b>

This is another short Python script which interacts with Google Spreadsheet. It also
utilizes smtplib, which is the standard Python library for sending emails over SMTP.
After reading in all the information from Google Docs/Drive, the script sends out
emails over a list of UNIs (used to form your Columbia email). This will be used to
send out grade reports for assignments.

<b>selenium script</b>

This encompasses both push_grades.sh as well as download_grade_zip.py. These
two scripts use Selenium to try and automate the transfer and pushing of
grades from Google Drive directly to Courseworks. The first selenium portion
of the scipt is working which is great news. Now this script needs to be 
expanded upon to perform actually import and exporting.
