#(same as A)
import socket
host = "127.0.0.1"
port = 45000

# Server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((host, port))
    server.listen(1)
    print("*Waiting on Program A*", flush=True)
    connection, _ = server.accept()

#read A
    with connection:
        with connection.makefile("r", encoding="utf-8") as message_file:
            message = message_file.readline()
#A uppercase, send back
        reply = message.upper()
        connection.sendall(reply.encode("utf-8"))