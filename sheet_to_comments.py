#!/usr/bin/env python

import gspread, os, getpass

#Get Google Drive credentials
username = raw_input('Drive Username: ')
password = getpass.getpass(prompt='Drive Password: ')
filename = raw_input('Drive Filename: ')
assignment_name = raw_input('Assignment Name: ')
column_number = raw_input('Total Grade Column Number: ')

#Log in
print "Logging into Google Drive"
gc = gspread.login(username, password)

#Open sheet
wks = gc.open(filename).sheet1

#Download
print "Downloading Data Ranges..."
i = 2
columns = []
while(i <= int(column_number)):
    columns.append(wks.col_values(i))
    i = i + 1

#Switch into correct directory and get list of directories
os.chdir("./Written1")
dirList = os.listdir("./")

#Write to file
print "Writing Data Ranges to File..."
i = 0
while i < len(columns[0]):
    os.chdir("./" + str(dirList[i+1]))
    with open("comments.txt", "w") as myfile:
        msg = ("Hi!\n\nHere is your " + str(assignment_name) + " Grade " + 
            "Report. Before you are tempted to reply to this email, please " +
            "read the general email that I sent first. If you have any " + 
            "questions, please refer to the info in that email and contact the " + 
            "TA who graded your homework. Your TA is the person who you can " +
            "ask for regrades on this assignment. If you cannot resolve " +
            "the issue with your TA, then please get in touch with me and " +
            "we will work it out together!\n\n")

        j = 1
        while(j < (int(column_number))-1):
            msg = msg + (columns[j][0] + ": " + 
                  str(columns[j][i+1]).encode('utf-8') + "\n")
            j = j + 1

        myfile.write(msg)
    os.chdir("..")
    i = i + 1


# while i < len(list1):
#     print "Editing files of " + str(dirList[i])
#     os.chdir("./" + str(dirList[i]))
#     with open("comments.txt", "w") as myfile:
#         myfile.write("Total: " + str(list0[i].value) + "/100\n\n")
#         myfile.write("Program 1: " + str(list1[i].value) + "/100\n")
#         #myfile.write("Written 2: " + str(list2[i].value) + "/5\n")
#         #myfile.write("Written 3: " + str(list3[i].value) + "/10\n")
#         #myfile.write("Written 4: " + str(list4[i].value) + "/10\n")
#         #myfile.write("Written 5: " + str(list5[i].value) + "/10\n")
#         #myfile.write("Program 1: " + str(list6[i].value) + "/30\n")
#         #myfile.write("Program 2: " + str(list7[i].value) + "/30\n\n")

#         myfile.write("Comments: " + (comment_list[i].value).encode('utf-8'))
#     os.chdir("..")
#     i = i + 1
