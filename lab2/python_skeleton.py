from socket import *
msgHeaders = "From: jonmmh8@gmail.com\r\nTo: vegard.klund@gmail.com\r\nSubject: Mail\r\n"
msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.stud.ntnu.no" #Fill in start   #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
serverport = 25
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverport))
#Fill in end
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = 'MAIL FROM: bla@bla.no\r\n'
clientSocket.send(mailFromCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server'
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = 'RCPT TO: vegard.klund@gmail.com\r\n'
clientSocket.send(rcptToCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server' 
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '354':
	print '354 reply not received from server' 
# Fill in end

# Send message data.
# Fill in start
message = raw_input('Write your e-mail: ')
# Fill in end
# Message ends with a single period.

# Fill in start
endMessage = raw_input('Enter a "." to exit message')

clientSocket.send(msgHeaders)
clientSocket.send(message)
if endMessage == '.':
	clientSocket.send("\r\n.\r\n")

recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server' 
# Fill in end

# Send QUIT command and get server response.
# Fill in start

quitCommand = 'QUIT\r\n'
clientSocket.send("QUIT\r\n")
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '221':
	print '221 reply not received from server'

# Fill in end
