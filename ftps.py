#!/usr/bin/env	python
# CSE 3461, Lab 3
# Sebastin Justeeson
# Server program

import socket
import os
import sys

# Symbolic name meaning all available interfaces
localHost = ''
localPort = int(sys.argv[1])   
print(localHost)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
serverSocket.bind((localHost, localPort))

directory = 'ReceivedFiles'
if not os.path.exists(directory):
    os.makedirs(directory)

print('waiting for package')
# Receive and write data until the loop is forced to break
while True:
		data, address = serverSocket.recvfrom(1000)
		data = data.decode('utf-8')
		if data == "": break
		# Find positions of local port and flag
		position = data.find(str(localPort))
		flag = data[position + len(str(localPort))]

		# Obtain file size, name and data
		if flag == '1':
				fileSize = int(data[position + len(str(localPort)) + 1:])
				print(fileSize)
		if flag == '2':
				newFileName = data[position + len(str(localPort)) + 1:]
				print(newFileName)
		if flag == '3':
				fileData = data[position + len(str(localPort)) + 1:]
				newFile = open('ReceivedFiles/'+newFileName, 'a+')
				print(fileData)
				newFile.write(fileData)
		
# Close all open streams
serverSocket.close()
newFile.close()

