import socket

def search_for_free_port(start_port):
    port = start_port
    while True:
        try:
            sock = socket.socket()
            sock.bind(('', port))
            print(f"Server is listening on port {port}")
            return sock, port
        except OSError:
            print(f"Порт {port} уже занят, попробуйте друнг.")
            port += 1

sock, port = search_for_free_port(9090)
sock.listen(0)
conn, addr = sock.accept()
print("Клиент принят")
print("Адрес клиента:", addr[0])
print("Порт клиента:", addr[1])

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()
