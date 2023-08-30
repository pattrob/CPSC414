#I pledge Patton Robertson
import sys, time
from socket import *

# Get the server hostname and port to receive them from command line arguments
argv = sys.argv     
host = '127.0.0.1'
port = 1024
timeout = 1 # timeout variable in second
 
# TODO-Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# TODO-Set clientSocket timeout as one second. You must use the 
#timeout variable created earlier to set this value.

clientSocket.settimeout(timeout)
# Command line argument is a string, change the port into integer
port = int(port)  
# Sequence number of the ping message
ptime = 0  

# Ping the server for 10 times
while ptime < 10: 
    ptime += 1
    # Create and format the UDP data packet or ping message to be sent to the server
    data = "Ping " + str(ptime) + " " + time.asctime()
    
    try:
	# Sent time
        RTTb = time.time()
	# TODO-Send the encoded UDP data packet or the ping message created earlier to the server (these are accepted as command line arguments earlier).
	# Send data to server: The data sent will be the ping message.
        clientSocket.sendto(data.encode(), (host, port))
        
	# TODO-Receive the server response and store it into variables named message and address
        message, address = (clientSocket.recvfrom(1024))
    
    #TODO-convert received message into a string
        recvmessage = message.decode()
             
	# TODO: Computer and store received time
        RTT = time.time()
        
	# TODO-Display or print the server response (both the address and message) and print the Round trip time.
        print(f"Reply from {address}: {message}")
        print(f"RTT: {RTT - RTTb}s")
        
    except:
        # Server does not response
	# Assume the packet is lost
        print("Request timed out.")
        continue

# TODO-Close the client socket
clientSocket.close()

 
