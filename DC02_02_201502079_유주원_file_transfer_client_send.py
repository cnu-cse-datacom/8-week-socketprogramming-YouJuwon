import socket
import os

ip_addr = "127.0.0.1"
port = "9000"

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

fileName = input("Input your file name : ")
socket.sendto(fileName.encode(), (ip_addr, int(port)))

f = open(fileName, 'rb')
fileSize = os.path.getsize(fileName)
socket.sendto(str(fileSize).encode(), (ip_addr, int(port)))
count=0
while True:
    s = f.read(1024)
    count += len(s)
    print("current_size / total_size = " + repr(count) + "/" + repr(fileSize) + ", " + repr( 100 * count / fileSize) + "%")
    socket.sendto(s, (ip_addr, int(port)))
    if s == '' or count >= fileSize:
        break
print("ok")
print("file_send_end")

