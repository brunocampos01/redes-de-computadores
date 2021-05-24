import socket
import json
import datetime


serverhost1 = '127.0.0.1'
serverport1 = 8000

# create object to connect server 1
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock.connect(serverhost1, serverport1) 

print('\t\t\t(@) Cliente 1')
msg = input('(#) Type a menssage: ')

data = {
    "verb": "sendto",
    "timestamp": str(datetime.datetime.now()),
    "payload": msg
}
j = json.dumps(data)

ClientSock.send(j.encode("utf-8"))
ServerMessage = ClientSock.recv(1000)
print('(OK) Message sent!')
print('\tMessage content --> '+ServerMessage.decode('utf-8'))

ClientSock.close()
