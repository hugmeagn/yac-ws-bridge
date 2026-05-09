# udp_echo.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 1080))
print('UDP echo listening on 127.0.0.1:1080')
while True:
    data, addr = s.recvfrom(65535)
    print(f'GOT: {data[:100]}... from {addr}')
    s.sendto(data, addr)  # echo back
