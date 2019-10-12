import socket
from socket import*
import sys

ip = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]

hostname = gethostbyaddr(ip)[1]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((hostname, port))

request = "GET /" + filename + "HTTP/1.1\r" 
clientSocket.send(request)
full_msg = ""
while 1:
    msg = clientSocket.recv(1000)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)

clientSocket.close()
