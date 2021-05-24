import socket
import json


host2 = '127.0.0.1'
port2 = 8001
client_port = 8003 # port that client 2 will connect to

# connection object created so that server1 (client) connects to server 2
ServerSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock2.bind(('', port2))
ServerSock2.listen(1)

# Server 2 acts as the same server and opens (on another port) for the client to connect
client_sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock2.bind(('',client_port))
client_sock2.listen(1)
print('(**) Server 2 started on('+str(host2)+':'+str(port2)+')')

while True:
    (NewClientSock1, addr2) = ServerSock2.accept()
    print('(@) Cliente connected ' + str(addr2))
    client_msg = NewClientSock1.recv(1000)
    
    if client_msg:
        (NewClientSock2, addrCli) = client_sock2.accept()
        d = json.loads(client_msg)
        print('(OK) Menssage received!')
        print('Message content: ' , d)
        NewClientSock2.send(client_msg)
