from socket import *
serverName = '10.213.156.171'
#pick any port number outside of 1024
serverPort = 2023
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('enter a message to send to server')
clientSocket.sendto(str.encode(message), (serverName, serverPort))
modifiedMsg, serverAddr = clientSocket.recvfrom(2048)
print(modifiedMsg)
clientSocket.close()