#!/usr/bin/env	python
# CSE 3461, Lab 3
# Sebastin Justeeson
# Client program

import socket
import os
import sys

remoteGammaAddress = sys.argv[1]   
remoteGammaPort = int(sys.argv[2])          
localTrollPort = int(sys.argv[3])
fileName = sys.argv[4]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSocket.bind(('', 3306)) 

file = open(fileName, 'rb')

# Create the segments and then send first 2 segments through socket
firstSegment = remoteGammaAddress + str(remoteGammaPort) + '1' + str(os.stat(fileName).st_size)
secondSegment = remoteGammaAddress + str(remoteGammaPort) + '2' + fileName
otherSegment = remoteGammaAddress + str(remoteGammaPort) + '3'
clientSocket.sendto(firstSegment.encode('utf-8'), ('', localTrollPort))
clientSocket.sendto(secondSegment.encode('utf-8'), ('', localTrollPort))
# Send data through socket while file is not empty
data = file.read(1000)
while data != b"":
	dataSegment = otherSegment + str(data)
	clientSocket.sendto(dataSegment.encode('utf-8'), ('', localTrollPort))
	data = file.read(1000)
	
clientSocket.close()
file.close()






