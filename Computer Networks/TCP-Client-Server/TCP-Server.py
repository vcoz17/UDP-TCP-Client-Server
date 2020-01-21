import socket
import re

def finOC(oc):
	operands = ['+','-','*',"/"]
	if not oc[1].isdigit() or not oc[2].isdigit() or oc[0] not in operands or oc[2] == str(0):
		return str("300 -1")
	else:
		intoc1 = int(oc[1])
		intoc2 = int(oc[2])
		if oc[0] == '+' :
			return "200 "+' '+str(oc[1])+' '+str(oc[0])+' '+str(oc[2])+' '+str(intoc1+intoc2)
		elif oc[0] == '-' :
			return "200 "+' '+str(oc[1])+' '+str(oc[0])+' '+str(oc[2])+' '+str(intoc1-intoc2)
		elif oc[0] == '*' :
			return "200 "+' '+str(oc[1])+' '+str(oc[0])+' '+str(oc[2])+' '+str(intoc1*intoc2)
		else:
			return "200 "+' '+str(oc[1])+' '+str(oc[0])+' '+str(oc[2])+' '+str(intoc1/intoc2)

def main():
    serverPort = 12000
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind(('localhost',serverPort))
    serverSocket.listen(1)
    print("Server on")
    while 1:
        connectionSocket, clientAddress = serverSocket.accept()
        message = connectionSocket.recv(1024)
        utf8_message = message.decode("utf-8")
        oc = re.split('\s+',utf8_message)
        modifiedMessage = finOC(oc).encode()    
        connectionSocket.send(modifiedMessage)
        connectionSocket.close()    

if __name__=="__main__":
	main()   
