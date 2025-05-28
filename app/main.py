import socket  # noqa: F401
import threading
     
def handler(connection, address):
    values = {}
    while True:

        data = connection.recv(1024)
        data = data.split(b'\r\n')
        if len(data) < 3:
            return 
        if data[2] == b"PING" :
            connection.sendall(b"+PONG\r\n")
        elif data[2] == b"ECHO":
            connection.sendall(b"+" +data[4]+b"\r\n")
        elif data[2] == b"SET":
            values[data[4]] = data[6]
            connection.sendall(b"+OK\r\n")
        elif data[2] == b"GET":
            connection.sendall(b"+" +values[data[4]]+b"\r\n")

def main():

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    

    while True:
        connection, address = server_socket.accept()
        threading.Thread(target=handler, args=(connection,address)).start()
    


if __name__ == "__main__":
    main()
