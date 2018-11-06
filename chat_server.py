#establish a server to receive connection from port 10000
import socket
import thread
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port=10000
s.bind(("",10000))
s.listen(1)
print("Socket Listrening")

con,addr=s.accept()
print("Connet from"),
print(addr[0]),
print(" port:"),
print(addr[1])

def send_to_client(s,port):
    while(1):
        data_send=str(raw_input("Send:"))
        if not data_send:
            break
        con.sendall(data_send)

    
thread.start_new_thread(send_to_client,(s,port))
while(1):
    data=con.recv(100)
    if not data:
        break;
        #continue;
    print("Receive:"),
    print(data)

print("Finish")
con.close()
