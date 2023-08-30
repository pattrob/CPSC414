# I pledge Patton Robertson
# UDPPingerServer.py

# We will need the following module to generate randomized lost packets
import random
from socket import *
#Create a port variable and assign a port number outside 0-1023

serverPort = 1024

# TODO-Create a UDP socket named serverSocket. Use IPv4.
serverSocket = socket(AF_INET, SOCK_DGRAM)


# TODO-bind serverSocket created earlier to accept connections on host and port number
# Work with HOST number which has worked for you with earlier programs. 
serverSocket.bind(('', serverPort))
#Print that the server is ready to receive connections
print("Ready to receive connection")
while True:
    # TODO-Generate random number in the range of 0 to 10 using random function and store it
    #This variable is later used in the if statement.
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # TODO-Capitalize the message received from the client and store it back in the
    #same variable named message which will be sent back to client
    message = message.upper()
    # If random variable (created earlier) is less is than 4, we consider the packet lost
    #and do not respond. This is to artificially induce packet loss.
    if rand < 4:
        continue
    # Otherwise, the server responds-send a server response here
    serverSocket.sendto(message, address)
