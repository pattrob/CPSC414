#!/usr/bin/python3
import socket
# host (internal/localhost) IP address and port
HOST = ''
# TODO: Assign a port number to be used later
PORT =
# open the file and read our value of Pi
f = open("pi.txt", "r")
pi = f.read()
# TODO: create your socket object and store it into a variable named sock to use
UDP
sock =
# allow us to reuse an address for restarts
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# TODO: set the socket host and port number PORT created earlier
# wait for a client to connect to us with the "pi" message
print("Waiting for a connection...")
# TODO: Receives the request message from the client
print("Sending pi to", address)
# send the digits of pi one by one
for digit in pi:
    sock.sendto(digit.encode(), address)
# send lots of the ending character (in case they are dropped)
for i in range(1000):
    sock.sendto(b"-", address)
print("Done!")
# TODO: close connections

