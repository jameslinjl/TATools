#!/usr/bin/env python

import smtplib
import gspread
import getpass
import os
import time


# Get Google Drive credentials
username = raw_input('Drive Username: ')
password = getpass.getpass(prompt='Drive Password: ')
filename = raw_input('Drive Filename: ')
assignment_name = raw_input('Assignment Name: ')
column_number = raw_input('Total Grade Column Number: ')

# Log in
print "Logging into Google Drive"
gc = gspread.login(username, password)

# Open worksheet
wks = gc.open(filename).sheet1

# Download
# Add all the columns as lists in big list (2d)
print "Downloading Data Ranges..."
i = 2
columns = []
while(i <= int(column_number)):
	columns.append(wks.col_values(i))
	i = i + 1

# Start email script
print "Start sending emails"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

# Get email credentials
username = raw_input('Email Username: ')
password = getpass.getpass(prompt='Email Password: ')
fromaddr = raw_input('Sender Address: ')

# Log in to the server
server.login(username, password)

# Write actual email
subject = "[DO NOT REPLY] " + str(assignment_name) + " Grading Report"
i = 1
while i < len(columns[0]):

	recvaddr = columns[0][i] + "@columbia.edu"
	msg = "From : %s\nTo: %s\nSubject: %s\n" %(fromaddr, recvaddr, subject)
	msg = msg + ("Hi!\n\nHere is your " + str(assignment_name) + " Grade " + 
	      "Report. Before you are tempted to reply to this email, please " +
	      "read the general email that I sent first. If you have any " + 
	      "questions, please refer to the info in that email and contact the " + 
	      "TA who graded your homework. Your TA is the person who you can " +
	      "ask for regrades on this assignment. If you cannot resolve " +
	      "the issue with your TA, then please get in touch with me and " +
	      "we will work it out together!\n\n")

	j = 1
	while(j < (int(column_number))-1):
		if columns[j][i] is None:
			columns[j][i] = ''
		msg = (msg + (columns[j][0] + ": " + 
			  columns[j][i].encode('utf-8')) + "\n")
		j = j + 1

	msg = msg + "\n\n--James Lin, Head TA"
	i = i + 1

	#Send actual email
	try:
		server.sendmail(fromaddr, recvaddr, msg)
		print "Successful send to " + recvaddr
	except smtplib.SMTPException:
		print "Error: unable to send"
		time.sleep(60)
		i = i - 1
