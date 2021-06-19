import socket

# socket.AF_INET - используем протокол ip4
# socket.AF_INET6 - протокол ip6
# socket.SOCK_DGRAM - UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# '' '0.0.0.0' '0' - резервируем порт на всех интерфейсах
sock.bind(("127.0.0.1", 8888))

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print("Message", result.decode("utf-8"))
