#connect to a server through port 10000, send and receive data
import socket
import thread
import sys

#HOST="127.0.0.1"
if len(sys.argv) != 2:
    print("Usage:{} ip".format(sys.argv[0]))
    exit()
HOST=sys.argv[1]
port = 10000
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, 10000))
except:
    print("Error:Check you Ip input")
    exit()
print("connected")

def recv_from_server(s,port):
    while(1):
        data=s.recv(100)
        if not data:
            break
        print("Receive:"),
        print(data)

thread.start_new_thread(recv_from_server,(s,port))
while(1):
    data_send=str(raw_input("Send:"))
    if not data_send:
        break
    s.sendall(data_send)
print("Exit")

