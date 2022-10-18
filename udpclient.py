import socket
PORT=65432
HOST="127.0.0.1"
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    
    while True:
        msg=input(">>>")
        msg=msg.encode()
        s.sendto(msg,(HOST,PORT))
        data,addr=s.recvfrom(1024)
        msg=data
        msg=msg.decode()
        print("recieved message: ",data,"from: ",addr)


