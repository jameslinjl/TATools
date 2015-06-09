# TA Tools, Columbia University

This repo is for little useful tools and scripts for doing TA stuff.

## Setup

It's very important to have the correct setup to use this repo. Courseworks is not very friendly to scripting, so it requires the following of some precise conventions. These can almost certainly be improved upon, so you are welcome to do so. Expect the first running of the script to have issues and subsequent runs to go much more smoothly.

Google Drive
1. Make sure you are using Columbia University's LionDrive.
2. Create a grading spreadsheet with a unique name with the following naming convention: <Course #><Spring/Summer/Fall><YEAR><Assignment Name>Grades . Example: 1004Spring2015Programming1Grades
3. See attached spreadsheet for example of formatting.

Courseworks (Columbia LMS)
1. Ensure you have TA permission enabled by your professor.
2. Make sure you and your professor are primarily using the 'Assignments' tab to create assignments rather than 'Gradebook'. These scripts will need to be modified in order to function with the latter.
3. Currently, there are several hardcoded values that you need to track down within Courseworks. These are: course URL, assignments path, and main iframe. These will be hardcoded into lines 9, 10, and 11 of your cloned or forked version of selenium_script.py. Contact me if you have trouble locating these.

## Basic Usage

```bash
./push_grades.sh

UNI: #enter uniXXXX
Password: #enter uniPassword
Assignment Listing CW: #enter 1 for top assignments listing, 2 for second, etc.

# re-enter the above information again (can be optimized, see issues)
```

```bash
python mail_script.py

Drive Username: #enter uniXXXX@columbia.edu
Drive Password: #enter your drive password, also the same as your LionMail device password
Drive Filename: #enter exact name of grading spreadsheet
Assignment Name: #enter name of assignment you want students to see
Total Grade Column Number: #enter the number of the column (A is 1, B is 2, etc) which contains total grades, rest of spreadsheet is scraped accordingly
```
