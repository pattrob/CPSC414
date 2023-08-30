#!/usr/bin/python3

from socket import *

# open the file and read our value of Pi
f = open("pi-1.txt", "r")
pi = f.read()

# TODO - put in these values
HOST = '192.168.1.169'
PORT = 4040

# TODO create our UDP socket and store it in a variable named sock
sock = socket(AF_INET, SOCK_DGRAM)
# send the request to the server
print("Sending the request...")
sock.sendto(b"pi", ((HOST, PORT)))

print("Receiving Pi...", end="")

# keep track of our version of pi
received = ""

# receive the digits of pi one by one
while True:
    digit, address = sock.recvfrom(1)
    digit = digit.decode()
    if digit == '-':
        break
    else:
        received = received + digit
sock.close()
print("Done!")


# TODO insert analysis code here
def med_character(str1, str2):
    cost = 0
    len1 = len(str1)
    len2 = len(str2)
    # output the length of other string in case the length of any of the string is zero
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
    # initializing a zero matrix
    accumulator = [[0 for x in range(len2)] for y in range(len1)]
    # initializing the base cases
    for i in range(0, len1):
        accumulator[i][0] = i
    for i in range(0, len2):
        accumulator[0][i] = i
    # we take the accumulator and iterate through it row by row.
    for i in range(1, len1):
        char1 = str1[i]
        for j in range(1, len2):
            char2 = str2[j]
            cost1 = 0
            if char1 != char2:
                cost1 = 2  # cost for substitution
            accumulator[i][j] = min(accumulator[i - 1][j] + 1, accumulator[i][j - 1] + 1, accumulator[i - 1][j - 1] + cost1)
    cost = accumulator[len1 - 1][len2 - 1]
    return cost


print(med_character(received, pi))

# TODO make a function call to the analysis code to compare the pi file read locally here and digits received from the server

