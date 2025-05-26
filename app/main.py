import socket  # noqa: F401
import threading

def handler(connection, address):
    while True:
        data = connection.recv(1024)
        if data:
            connection.sendall(b"+PONG\r\n")

def main():

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    

    while True:
        connection, address = server_socket.accept()
        threading.Thread(target=handler, args=(connection,address)).start()
    


if __name__ == "__main__":
    main()
