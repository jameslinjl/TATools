#!/usr/bin/env python

import smtplib, gspread, getpass

#Get Google Drive credentials
username = raw_input('Drive Username: ')
password = getpass.getpass(prompt='Drive Password: ')
filename = raw_input('Drive Filename: ')

#Log in
print "Logging into Google Drive"
gc = gspread.login(username, password)

#Open worksheet
wks = gc.open(filename).sheet1

#Download
print "Downloading Data Ranges..."
recvaddrlst = wks.range('B101:B190')
list1 = wks.range('C101:C190')
list2 = wks.range('D101:D190')
list3 = wks.range('E101:E190')
list4 = wks.range('F101:F190')
list5 = wks.range('G101:G190')
list6 = wks.range('H101:H190')
#list7 = wks.range('I102:I199')
list8 = wks.range('I101:I190')
#list9 = wks.range('K102:K199')
comment_list = wks.range('J101:J190')
list10 = wks.range('M101:M190')

#Start email script
print "Start sending emails"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

#Get email credentials
username = raw_input('Email Username: ')
password = getpass.getpass(prompt='Email Password: ')
fromaddr = raw_input('Sender Name: ')

#Log in to the server
server.login(username, password)

#Write actual email
subject = "HW4 Comments"
i = 0
while i < len(recvaddrlst):
	recvaddr = str(recvaddrlst[i].value) + "@columbia.edu"
	msg = "From : %s\nTo: %s\nSubject: %s\n" %(fromaddr, recvaddr, subject)
	msg = msg + "Hi!\n\nHere is your HW4 Grade Report. If you did not turn in your homework through Courseworks, this grading report may not be accurate yet. If you have any questions, please refer to my general email and contact the TA who graded the question in mind. The grading rubric will be out soon.\n\n"
	msg = msg + "Written 1: " + str(list1[i].value) + "/5\n"
	msg = msg +	"Written 2: " + str(list2[i].value) + "/10\n"
	msg = msg + "Written 3: " + str(list3[i].value) + "/10\n"
	msg = msg + "Written 4: " + str(list4[i].value) + "/5\n"
	msg = msg + "Written 5: " + str(list5[i].value) + "/10\n"
	msg = msg + "Written 6: " + str(list6[i].value) + "/10\n"
	#msg = msg + "Written 7: " + str(list7[i].value) + "/10\n"
	msg = msg + "Program 1: " + str(list8[i].value) + "/50\n"
	#msg = msg + "Program 2: " + str(list9[i].value) + "/25\n\n"
	msg = msg + "Total: " + str(list10[i].value) + "/100\n\n"
	msg = msg + "Comments: \n" + (comment_list[i].value).encode('utf-8') + "\n\n\n"
	msg = msg + "--James Lin, Head TA"
	i = i + 1

	#Send actual email
	try:
		server.sendmail(fromaddr, recvaddr, msg)
		print "Successful send to " + recvaddr
	except smtplib.SMTPException:
		print "Error: unable to send"

