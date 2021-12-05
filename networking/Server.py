import socket #B317 - 172.17.17.80

# 2 types of sockets
# 1st socket (server socket) - listen to client connection requests
# 2nd socket - carry out communication (data transfer) with client

# 1. Create a server socket
# 2. Bind socket with port number
# 3. Listen to client connection requests using server socket

# 4. accept client connection and create socket for communication with connected client
# 5. initiate data transfer - data is to be converted in bytes form and after that we can transfer data
# 6. send() - to send data and recv() - to receive data

#Step1: Create a server socket
#The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address family ipv4. 
#The SOCK_STREAM means connection oriented TCP protocol and socket.SOCK_DGRAM means UDP protocol

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server Socket Created")

    #Step 2: bind server socket to specific port number
    s.bind(("localhost", 9999))#0-65535

    #Step 3: start listening to 3 client connections on server socket
    s.listen(3)
    print("Waiting for connections........")

    while True:
        #Step 4: Accept client connections
        c, addr = s.accept()

        print('Connected with',addr,c)

        #Send data to client
        toclient = bytes('Welcome !','utf-8')
        c.send(toclient)
        
        #server receives data from client
        fromclient = c.recv(1024).decode()
        print(fromclient)        
        
        #close client connection
        c.close()
except Exception as e:
    print(e)