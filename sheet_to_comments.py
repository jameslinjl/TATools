#!/usr/bin/env python

import gspread, os, getpass

#Get Google Drive credentials
username = raw_input('Drive Username: ')
password = getpass.getpass(prompt='Drive Password: ')
filename = raw_input('Drive Filename: ')

#Log in
print "Logging into Google Drive"
gc = gspread.login(username, password)

#Open sheet
wks = gc.open(filename).sheet1

#Download
print "Downloading Data Ranges..."
list0 = wks.range('F2:F189')
list1 = wks.range('C2:C189')
#list2 = wks.range('D2:D189')
#list3 = wks.range('E2:E189')
#list4 = wks.range('F2:F189')
#list5 = wks.range('G2:G189')
#list6 = wks.range('H2:H189')
#list7 = wks.range('I2:I189')
#list8 = wks.range('J2:J190')
#list9 = wks.range('K2:K190')
comment_list = wks.range('D2:D189')

#Switch into correct directory and get list of directories
os.chdir("./Homework 6")
dirList = os.listdir("./")

#Write to file
print "Writing Data Ranges to File..."
i = 0
while i < len(list1):
    print "Editing files of " + str(dirList[i])
    os.chdir("./" + str(dirList[i]))
    with open("comments.txt", "w") as myfile:
        myfile.write("Total: " + str(list0[i].value) + "/100\n\n")
        myfile.write("Program 1: " + str(list1[i].value) + "/100\n")
        #myfile.write("Written 2: " + str(list2[i].value) + "/5\n")
        #myfile.write("Written 3: " + str(list3[i].value) + "/10\n")
        #myfile.write("Written 4: " + str(list4[i].value) + "/10\n")
        #myfile.write("Written 5: " + str(list5[i].value) + "/10\n")
        #myfile.write("Program 1: " + str(list6[i].value) + "/30\n")
        #myfile.write("Program 2: " + str(list7[i].value) + "/30\n\n")

        myfile.write("Comments: " + (comment_list[i].value).encode('utf-8'))
    os.chdir("..")
    i = i + 1
