import socket
import time

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # настраиваем сокет
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # отключаем пакетирование
main_socket.bind(("localhost", 10000))  # ip и порт привязываем к порту
main_socket.setblocking(False)  # непрерывность, не ждем ответа
main_socket.listen(5)  # прослушка входящих соединений, 5 одновременных подключений
print("Сокет создался!")

players = []
while True:
    try:
        new_socket, addr = main_socket.accept()
        print("подключился", addr)
        new_socket.setblocking(False)
        players.append(new_socket)
    except BlockingIOError:
        pass
    for sock in players:  # Отправляем статус игрового поля
        try:
            sock.send("Игра".encode())
        except:
            players.remove(sock)
            sock.close()
            print("Сокет закрыт")
    time.sleep(1)
