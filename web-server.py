#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 12001))  
serverSocket.listen(1) 

while True:
#Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024) #Fill in start #Fill in end
        filename = message.split()[1]
        
        f = open(filename[1:])
        outputdata = f.read() #Fill in start #Fill in end
    
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode('utf-8'))
        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError as e:
        
        connectionSocket.send('HTTP/1.0 404 NOT FOUND\r\n\r\n'.encode('utf-8'))
        connectionSocket.send(f"{str(filename[1:])} not found. :)".encode('utf-8'))
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        pass
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
