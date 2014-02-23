#import socket module
from socket import *


serverPort = 12003
#Prepare a server socket (the welcoming socket/door)
#Creates the servers TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
#assigns the serverPort number to the servers socket
serverSocket.bind(("129.241.164.16",serverPort))

#Makes the server listen for TCP connection requests from the client. Parameter specifies
#maximum number of queued connections. Must be at least 1
serverSocket.listen(1)
print ('The server is ready to receive requests')

while True:
	#Establish the connection
	print ('Ready to serve...')

	#connectionSocket is is the newly created socket dedicated to the client making the connection
	#when a client knocks on this door the program invokes accept, witch creates a new socket in the
	#server called connectionSocket, dedicate to the particular client. The client and server now complete the handshaking
	#, creating a TCP connection between the clients clientSocket and the servers connectionSocket. They can now exchange 
	#bytes over the connection
	connectionSocket, addr = serverSocket.accept()

	try:

		message = connectionSocket.recv(1024)
		print '\n' + message + '\n'

		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		#Send one HTTP header line into socket

		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n404 Not Found")

		connectionSocket.close()

serverSocket.close()
