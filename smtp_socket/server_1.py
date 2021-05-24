import socket


host_1 = '127.0.0.1'
host_2 = '127.0.0.1'
port_1 = 8000
port_2 = 8001

# Server 1 must serve client 1
ServerSock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock1.bind(('', serverport1)) # connect server 1 to port 1
ServerSock1.listen(1)
print('(*) Server 1 started on ('+str(host_1)+':'+str(port_1)+')')

ServerSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock2.connect((host_2, port_2))

while True:
    (NewClientSock1, addr1) = ServerSock1.accept()
    print('(@) Client connected ' + str(addr1))
    ClientMessage = NewClientSock1.recv(1000)
    
    if ClientMessage:
        print('(#) Message received from customer --> '+ClientMessage.decode("utf-8"))
        NewClientSock1.send(ClientMessage)
    
    # server 1 connects with server 2
    # server 1 now behaves like a "client" to connect to
    print('\n(**) Sending msg to server 2...')
    print('(OK) Message sent!')
    ServerSock2.send(ClientMessage)
    
    NewClientSock1.close()
