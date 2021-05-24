import socket
import json


host_2 = '127.0.0.1'
port = 8003

client_sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock2.connect((host_2, port)) # connects to the dedicated server 2 created "client" port
print('\t\t(@) Client 2')

print('(WAIT) Waiting for message from client 1 ...')
server_message2 = client_sock2.recv(1000)
client_sock2.send(server_message2)
d2 = json.loads(server_message2)

print('(OK) Message received')
print('Message content: ',d2)
