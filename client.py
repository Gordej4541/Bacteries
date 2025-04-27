import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # настраиваем сокет
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # отключаем пакетирование
sock.connect(("localhost", 10000))
while True:
    sock.send("Привет!".encode())
