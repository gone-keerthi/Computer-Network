# echo-server.py
import socket
from datetime import datetime
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# AF_INET = ipv4
# SOCK_STREAM = tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("socket succesfully created")
    s.bind((HOST, PORT))
    print(f"socket succesfully binded to {PORT}")
    s.listen()
    print("socket is listening")
    connection, addr = s.accept()
    
    print(f"Connected by {addr}")
    while True:
        msg = input(">>> ")
        msg = msg.encode()
        connection.sendall(msg)
        msg = connection.recv(1024)
        msg = msg.decode()
        print("[{0}]: {1}".format(addr,msg))
        if msg == 'exit':
            connection.sendall("exit".encode())
            break

    connection.close()
    print("Connection Closed...")