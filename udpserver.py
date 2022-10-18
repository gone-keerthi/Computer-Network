import socket
PORT=65432
HOST="127.0.0.1"
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    print("socket succesfully created")
    s.bind((HOST,PORT))
    print(f"socket succesfully binded to {PORT}")
    
    while True:
        data,addr=s.recvfrom(1024)
        msg=data
        msg=msg.decode()
        print("recived message: ",data,"from: ",addr) 
        msg=input(">>>")
        msg=msg.encode()
        s.sendto(msg,(HOST,PORT))
