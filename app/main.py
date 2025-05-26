import socket  # noqa: F401


def init_server(address, port):
    server_socket = socket.create_server((address, port), reuse_port=True)
    connection, address = server_socket.accept()
    return connection, address

def main():

    connection, _ =init_server("localhost", 6379)
    while True:
        data = connection.recv(1024)
        stringdata = data.decode('utf-8').strip()
        if not data:
            break
        if "PING" in stringdata:
            connection.sendall(b"+PONG\r\n")
        else:
            break
    
    


if __name__ == "__main__":
    main()
