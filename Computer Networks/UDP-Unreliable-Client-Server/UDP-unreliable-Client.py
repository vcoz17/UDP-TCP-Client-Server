import socket
import re
import sys
import time

def myTimer():
    print("Hi")

def main():
    serverName = 'localhost'
    serverPort = 12000
    file = open(sys.argv[1],"r")
    ct = 0
    while ct < 6:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        d = 0.1
        line = file.readline()
        while 1:
            clientSocket.sendto(line.encode(),(serverName, serverPort))
            time.sleep(d)
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            if len(modifiedMessage.decode()) != 4:
                decodedms = re.split('\s+',modifiedMessage.decode())
                if decodedms[0] == '300':
                    print('Status code: 300. There is an error. Please check your input!')
                elif decodedms[0] == '200':
                    print('Status code: 200. ' + 'The result of ' + decodedms[1] + ' ' + decodedms[2] + ' '+ decodedms[3] +' is: '+ decodedms[4])
                clientSocket.close()
                break
            else:
                d *= 2
                if d > 2:
                    print('There is an error. The server might be DEAD.\n') 
                    break                  
        ct += 1

if __name__=="__main__":
	main()
