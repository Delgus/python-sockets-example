import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
sock.setblocking(False)
# sock.settimeout(5)
# sock.settimeout(0) -> sock.setblocking(False)
# sock.settimeout(None) -> sock.setblocking(True)

while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print('no clients')
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        client.setblocking(True)
        result = client.recv(1024)
        client.close()
        print('Message', result.decode('utf-8'))
