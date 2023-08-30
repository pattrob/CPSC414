from socket import *
import os
import sys
import struct
import time
import select
import binascii  
		
ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT  = 3.0 
TRIES    = 2

# The packet that we shall send to each router along the path is the ICMP echo
# request packet, which is exactly what we had used in the ICMP ping exercise.
# We shall use the same packet that we built in the Ping exercise

def checksum(stri: str): 
	#Fill in Start
	csum = 0
	countTo = (len(stri) / 2) * 2

	count = 0
	while count < countTo:
		thisVal = ord(chr(stri[count + 1])) * 256 + ord(chr(stri[count]))
		csum = csum + thisVal
		csum = csum & 0xffffffff
		count = count + 2

	if countTo < len(stri):
		csum = csum + ord(stri[len(stri) - 1])
		csum = csum & 0xffffffff

	csum = (csum >> 16) + (csum & 0xffff)
	csum = csum + (csum >> 16)
	answer = ~csum
	answer = answer & 0xffff
	answer = answer >> 8 | (answer << 8 & 0xff00)
	return answer
	# In this function we make the checksum of our packet
	# hint: see icmpPing part of the lab 
	#Fill in End

def build_packet():
	#Fill in Start
	myChecksum = 0
	ID = os.getpid() & 0xFFFF

	# For an ICMP echo request the header contains each of size (#bits)
	# Header is type (8), code (8), checksum (16), ID (16), sequence (16)
	#In the sendOnePing() method of the ICMP Ping exercise ,firstly the header of our
	# packet to be sent was made, secondly the checksum was appended to the header and
	# then finally the complete packet was sent to the destination.
	# Make the header in a similar way to the ping exercise.

	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
	data = struct.pack("d", time.time())
	# Append checksum to the header.
	myChecksum = checksum(header + data)
	if sys.platform == 'darwin':
		myChecksum = htons(myChecksum) & 0xffff
	# Convert 16-bit integers from host to network byte order.
	else:
		myChecksum = htons(myChecksum)
	# Don’t send the packet yet , just return the final packet in this function.
	# So the function ending should look like this
	#packet = header + data
	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
	packet = header + data
	#return packet
	return packet
	#Fill in end 


def get_route(hostname):
	timeLeft = TIMEOUT
	for ttl in range(1,MAX_HOPS):
		for tries in range(TRIES):
			#Fill in Start
			#get the IP address of the hostname variable passed
			destAddr = gethostbyname(hostname)
			#Fill in end
			#Fill in Start
			icmp = getprotobyname("icmp")
			mySocket = socket(AF_INET, SOCK_RAW, icmp)
			#Make a raw socket to use icmp, use the name mysocket 
			#Fill in end
			mySocket.bind(("", 0))
			# setsockopt method is used to set the time-to-live field. 
			mySocket.setsockopt(IPPROTO_IP, IP_TTL, struct.pack('I', ttl))
			mySocket.settimeout(TIMEOUT)
			try:
				d = build_packet()
				mySocket.sendto(d, (hostname, 0))
				t= time.time()
				startedSelect = time.time()
				whatReady = select.select([mySocket], [], [], timeLeft)
				howLongInSelect = (time.time() - startedSelect)
				if whatReady[0] == []: # Timeout
					# Fill in Start
					print("Request timed out to " + destAddr)
					# print request timed out to destination address
					#Fill in End
				recvPacket, addr = mySocket.recvfrom(1024)
				timeReceived = time.time()
				timeLeft = timeLeft - howLongInSelect
				if timeLeft <= 0:
					# Fill in Start
					print("Request timed out to " + destAddr)
					# print request timed out to destination address
					#Fill in End
				
			except timeout:
				continue			
			
			else:
				# Fill in Start
				# Fetch the ICMP type and code from the received packet

				icmpHeader = recvPacket[20:28]
				type, code, checksum, packetID, sequence = struct.unpack("bbHHh", icmpHeader)
				print("Type: " + str(type))
				print("Code: " + str(code))


				#Fill in End
				
				
				if type == 11:
					bytes = struct.calcsize("d") 
					timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
					print("  %d    rtt=%.0f ms    %s" %(ttl, (timeReceived -t)*1000, addr[0]))
				
				elif type == 3:
					bytes = struct.calcsize("d") 
					timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
					print("  %d    rtt=%.0f ms    %s" %(ttl, (timeReceived-t)*1000, addr[0])) 
				
				elif type == 0:
					bytes = struct.calcsize("d") 
					timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
					print("  %d    rtt=%.0f ms    %s" %(ttl, (timeReceived - timeSent)*1000, addr[0]))
					return
			
				else:
					print("error")				
				break	
			finally:				
				mySocket.close()


get_route("google.com")

