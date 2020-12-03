import socket
from socket import *
import sys

severHost = sys.argv[1]
severPort = sys.argv[2]
fileName = sys.argv[3]

hostPort = f"{severHost}:{severPort}"

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((severHost, int(severPort)))
    
    httpHead = {
	"first_header" : f"GET /{fileName} HTTP/1.1",
    "Host": hostPort,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-us"
	
	}
    httpHead = "\r\n".join(f"{item}:{httpHead[item]}"for item in httpHead)
    
    clientSocket.send(f"{httpHead}\r\n\r\n".encode())

except IOError as e:
    print(str(e))
    sys.exit(1)

 #C:/Users/Timothy/AppData/Local/Programs/Python/Python39-32/python.exe c:/Users/Timothy/Documents/GitHub/CS3840/client.py localhost 12001 file.txt


datas = []
while True:
    data = clientSocket.recv(1024)
    if data: # after getting the first data
        datas.append(str(data))
    else:
        break
print("The HTTP response is: ", ''.join(datas))