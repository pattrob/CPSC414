
from socket import *
from datetime import *
serverPort = 2023
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('server is ready to receive requests')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMsg = datetime.strftime('%A, %B %d, %Y, %I:%M %p\n')
    serverSocket.sendto(str.encode(modifiedMsg), clientAddress)
