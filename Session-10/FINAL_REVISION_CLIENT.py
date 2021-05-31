import socket

PORT = 8080  # Server
IP = "127.0.0.1"  # Server

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect((IP, PORT))  # gives to my_socket an IP and a Port

msg = "HELLO FROM THE CLIENT!!!"  # str
my_socket.send(str.encode(msg))  # Codify: str -> bytes

b = my_socket.recv(2048)
msg = b.decode("utf-8")  # Decodify: bytes -> str
print(f"MSG: {msg}")

my_socket.close()
