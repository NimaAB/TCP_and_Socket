import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((socket.gethostname(),1234))

msg1 = clientSocket.recv(1024)    
print(msg1.decode("utf-8"))

disconnect_req = input()
clientSocket.send(disconnect_req.encode())
    
msg2 = clientSocket.recv(1024) 
print(msg2.decode("utf-8"))
