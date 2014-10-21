import gspread, os

#Get Google Drive credentials
username = raw_input('Drive Username: ')
password = raw_input('Drive Password: ')
filename = raw_input('Drive Filename: ')

#Log in
print "Logging into Google Drive"
gc = gspread.login(username, password)

#Open sheet
wks = gc.open(filename).sheet1

#Download
print "Downloading Data Ranges..."
list1 = wks.range('C2:C199')
list2 = wks.range('D2:D199')
list3 = wks.range('E2:E199')
list4 = wks.range('F2:F199')
list5 = wks.range('G2:G199')
list6 = wks.range('H2:H199')
list7 = wks.range('I2:I199')
list8 = wks.range('J2:J199')
list9 = wks.range('K2:K199')
comment_list = wks.range('L2:L199')

#Switch into correct directory and get list of directories
os.chdir("./Homework 2-1")
dirList = os.listdir("./")

#Write to file
print "Writing Data Ranges to File..."
i = 0
while i < len(list1):
	os.chdir("./" + str(dirList[i+1]))
	with open("comments.txt", "w") as myfile:
		myfile.write("Written 1: " + str(list1[i].value) + "/10\n")
		myfile.write("Written 2: " + str(list2[i].value) + "/5\n")
		myfile.write("Written 3: " + str(list3[i].value) + "/5\n")
		myfile.write("Written 4: " + str(list4[i].value) + "/10\n")
		myfile.write("Written 5: " + str(list5[i].value) + "/5\n")
		myfile.write("Written 6: " + str(list6[i].value) + "/5\n")
		myfile.write("Program 1: " + str(list7[i].value) + "/20\n")
		myfile.write("Program 2: " + str(list8[i].value) + "/20\n")
		myfile.write("Program 3: " + str(list9[i].value) + "/20\n\n")

		myfile.write("Comments: " + (comment_list[i].value).encode('utf-8'))
	os.chdir("..")
	i = i + 1
