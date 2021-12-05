import socket #B215

#Step 1: create a socket
c = socket.socket()#by default initialized with following parameters: socket.AF_INET, socket.SOCK_STREAM

#Step 2: connect to server
c.connect(('localhost', 9999))#pass server IP address and port number

print('Connected')

#Recieve data from server
    #1024- no. of bytes to receive.
    #recv() can be used with both, TCP and UDP sockets. 
    #It returns the received data as byte object

fromserver = c.recv(1024).decode()
print(fromserver)
print(type(fromserver))

#client sends data to server
toserver = bytes('Hello from Client-3','utf-8')
c.send(toserver)


#c.close()




