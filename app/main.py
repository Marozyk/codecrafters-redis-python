import socket  # noqa: F401
import threading
import time
     
def handler(connection, address):
    values = {}
    timers = {}
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
            if data[7] == b"px":
                timers[data[4]] = time.time + (data[8]/1000)
            connection.sendall(b"+OK\r\n")
        elif data[2] == b"GET":
            if data[4] in timers:
                if time.time() >= timers[key]:
                    connection.sendall(b"$-1\r\n")
                    timers.pop(data[4])
            else:
                connection.sendall(b"+" +values[data[4]]+b"\r\n")

def main():

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    

    while True:
        connection, address = server_socket.accept()
        threading.Thread(target=handler, args=(connection,address)).start()
    


if __name__ == "__main__":
    main()
