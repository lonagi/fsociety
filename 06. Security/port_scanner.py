import socket
import subprocess
import sys
from datetime import datetime

# Ask for input
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(1,10250):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()
except:
    pass

t2 = datetime.now()
total =  t2 - t1
print('Scanning Completed in: ', total)