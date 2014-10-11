import smtplib, gspread

#Get Google Drive credentials
username = raw_input('Drive Username: ')
password = raw_input('Drive Password: ')
filename = raw_input('Drive Filename: ')

#Log in
print "Logging into Google Drive"
gc = gspread.login(username, password)

#Open worksheet
wks = gc.open(filename).sheet1

#Download
print "Downloading Data Ranges..."
recvaddrlst = wks.range('B2:B3')
list1 = wks.range('C2:C3')
list2 = wks.range('D2:D3')
list3 = wks.range('E2:E3')
list4 = wks.range('F2:F3')
list5 = wks.range('G2:G3')
list6 = wks.range('H2:H3')
list7 = wks.range('I2:I3')
list8 = wks.range('J2:J3')
list9 = wks.range('K2:K3')
comment_list = wks.range('L2:L3')

#Start email script
print "Start sending emails"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

#Get email credentials
username = raw_input('Email Username: ')
password = raw_input('Email Password: ')
fromaddr = raw_input('Sender Name: ')

#Log in to the server
server.login(username, password)

#Write actual email
subject = "HW1 Comments"
i = 0
while i < len(recvaddrlst):
	recvaddr = str(recvaddrlst[i].value) + "@columbia.edu"
	msg = "From : %s\nTo: %s\nSubject: %s\n" %(fromaddr, recvaddr, subject)
	msg = msg + "Hi!\n\nHere is your HW1 Grade Report. If you have any questions, please email cs3134staff@lists.cs.columbia.edu\n\n"
	msg = msg + "Written 1: " + str(list1[i].value) + "/10\n"
	msg = msg +	"Written 2: " + str(list2[i].value) + "/10\n"
	msg = msg + "Written 3: " + str(list3[i].value) + "/10\n"
	msg = msg + "Written 4: " + str(list4[i].value) + "/10\n"
	msg = msg + "Written 5: " + str(list5[i].value) + "/10\n"
	msg = msg + "Written 6: " + str(list6[i].value) + "/10\n"
	msg = msg + "Program 1: " + str(list7[i].value) + "/10\n"
	msg = msg + "Program 2: " + str(list8[i].value) + "/10\n"
	msg = msg + "Program 3: " + str(list9[i].value) + "/10\n\n"
	msg = msg + "Comments: " + comment_list[i].value + "\n\n\n"
	msg = msg + "--James Lin, Head TA"
	i = i + 1

	#Send actual email
	try:
		server.sendmail(fromaddr, recvaddr, msg)
		print "Successful send to " + recvaddr
	except smtplib.SMTPException:
		print "Error: unable to send"

