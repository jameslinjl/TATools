import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

username = raw_input('Username: ')
password = raw_input('Password: ')
fromaddr = raw_input('Sender Address: ')
recvaddr = raw_input('Receiver Address: ')

#password = "QdT4yG$N"

#Next, log in to the server
server.login(username, password)

#while loop
#use sheet_to_comments except write to a single message
#make sure to get UNI too in order to send to correct email
#send out email

#Send the mails
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail(fromaddr, recvaddr, msg)
