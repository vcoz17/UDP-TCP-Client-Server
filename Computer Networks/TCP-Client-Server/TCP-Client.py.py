import socket
import re
import sys

def main():
    serverName = 'localhost'
    serverPort = 12000
    file = open(sys.argv[1],"r")
    ct = 0
    while ct < 6:
        clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
        line = file.readline()
        clientSocket.send(line.encode())
        modifiedMessage = clientSocket.recv(1024) 
        decodedms = re.split('\s+',modifiedMessage.decode())
        if decodedms[0] == '300':
            print('Status code: 300. There is an error. Please check your input!')
        elif decodedms[0] == '200':
            print('Status code: 200. ' + 'The result of ' + decodedms[1] + ' ' + decodedms[2] + ' '+ decodedms[3] +' is: '+ decodedms[4])
        clientSocket.close()
        ct += 1

if __name__=="__main__":
	main()
