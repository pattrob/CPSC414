import argparse
import sys, time
from socket import *


def scan_ports(host, start_port, end_port, protocol):
    # setup
    global sock
    print("Scanning: " + host + " From port: " + str(start_port) + " To Port: " + str(end_port))
    # Create Socket in the try block
    try:
        # TODO-Create a TCP or UDP socket object depending on protocol using conditional statements
        if protocol == "UDP":
            sock = socket(AF_INET, SOCK_DGRAM)
        elif protocol == "TCP":
            sock = socket(AF_INET, SOCK_STREAM)
        else:
            raise ValueError(protocol + " is not valid protocol")


    # setting socket to timeout
        sock.settimeout(1)
    except:
    # TODO-handle the error
        print("Cannot create socket.")


    # Set the IP
    remote_ip = host
    # TODO-print the IP address you are scanning
    print(remote_ip)

    # Scan Ports
    end_port += 1
    # TODO-loop over the range of ports and try connecting to them individually
    for i in range(start_port, end_port):
        try:
            if protocol == "TCP":
                create_connection((host, i))
                print(f"TCP Port {i} is open")
            elif protocol == "UDP":
                message = "test"
                sock.sendto(message, (host, i))
                data, server = sock.recvfrom(i)
                print(f"UDP Port {i} is open")
        except:
                print(f"{protocol} Port {i} is closed")

    sock.close()




# TODO-make use of exception handlers to handle any exceptions thrown


# parsing stuff you dont have to change
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remote Port Scanner')
    # setting the IP address to scan
    parser.add_argument('--host', action="store", dest="host", default='127.0.0.1')
    # setting the starting port no.
    parser.add_argument('--start-port', action="store", dest="start_port", default=1, type=int)
    # setting the ending port no.
    parser.add_argument('--end-port', action="store", dest="end_port", default=100, type=int)
    # setting the default protocol to scan for
    parser.add_argument('--protocol', action="store", dest="protocol", default="TCP")
# parse args
given_args = parser.parse_args()
host, start_port, end_port, protocol = given_args.host, given_args.start_port, given_args.end_port, given_args.protocol
scan_ports(host, start_port, end_port, protocol)
