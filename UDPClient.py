from socket import *
serverName = "10.213.156.171"
serverPort = 2023
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("send a date/time request to the server by inputting a character")
clientSocket.sendto(str.encode(message), (serverName, serverPort))
modifiedMsg, serverAddr = clientSocket.recvfrom(2048)
print(modifiedMsg)
clientSocket.close()

