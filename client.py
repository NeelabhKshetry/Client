import socket
from socket import*
import sys

ip = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]

hostname = gethostbyaddr(ip)[1]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((hostname, port))

try:
    f = open(filename, "utf-8")
    outputdata = f.read()
    clientSocket.send(bytes("HTTP/1.1 200 OK", "utf-8"))

    for i in range(0, len(outputdata)):
        clientSocket.send(bytes(outputdata[i], "utf-8"))
except IOError:
    # Send response message for file not found
    clientSocket.send(bytes("HTTP/1.1 404 Not Found\r\n", "utf-8"))

    errorfile = open("ErrorPage.html", encoding="utf-8")
    errormessage = errorfile.read()

    for i in range(0, len(errormessage)):
        clientSocket.send(bytes(errormessage[i], "utf-8"))

    # Close client socket
    clientSocket.close()
