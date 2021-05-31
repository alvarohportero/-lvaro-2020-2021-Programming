import socket

PORT = 8080  # Server
IP = "localhost"  # Server

try:
    while True:
        msg = input(">> ")

        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        my_socket.connect((IP, PORT))  # gives to my_socket an IP and a Port

        my_socket.send(str.encode(msg))  # Codify: str -> bytes

        my_socket.close()
except KeyboardInterrupt:
    print("Client stopped by the user")
