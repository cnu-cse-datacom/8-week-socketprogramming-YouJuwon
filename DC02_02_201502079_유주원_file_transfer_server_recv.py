import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('',9000))
fileName, addr = socket.recvfrom(2000)

print("file recv start from " + addr[0])
print("File Name : " + fileName.decode())
fileSize, addr = socket.recvfrom(2000)
print("File Size : " + repr(fileSize))
count =0
f = open("recv" + fileName.decode(),'wb')
while True:
    data, addr = socket.recvfrom(2000)
    count += len(data)
    print("current_size / total_size = " + repr(count) + "/" + str(fileSize.decode()) + ", " + repr( 100 * count / int(fileSize)) + "%")
    f.write(data)
    if count >= int(fileSize):
        break
