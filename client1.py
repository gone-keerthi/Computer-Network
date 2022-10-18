# echo-client.py
import socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = s.recv(1024)
        msg = msg.decode()
        print("[{0},{1}]: {2}".format(HOST,PORT,msg))
        if msg == 'exit':
            s.sendall("exit".encode())
            break
        msg = input(">>> ")
        msg = msg.encode()
        s.sendall(msg)
    print("Connection Closed...")
    