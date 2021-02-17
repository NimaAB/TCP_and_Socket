import socket

'''
server.py listening for a client to connect to given ip-address and port.
once the client is connected the server will send back a encoded message to the
client and close the connection.
'''

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((socket.gethostname(),1234))
serverSocket.listen(6)

while True:
    print('listening for connection...')
    (clientSocket, address) = serverSocket.accept()
    print(f"Conection with {address} established!")
    clientSocket.send("Connection established! Hello!".encode())
    
    disconnect_msg = clientSocket.recv(1024).decode("utf-8")
    if disconnect_msg == "Bye":
        clientSocket.send("You are now disconnected, Bye".encode())
        clientSocket.close()
        break


