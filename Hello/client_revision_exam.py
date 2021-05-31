import socket

PORT = 8080  # servidor
IP = "127.0.0.1"  # SERVIDOR

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect((IP, PORT))  # ASOCIA A MI SOCKET LA IP LOCAL Y UN PUERTO LIBRE ALEATORIO

msg_1 = "HELLO FROM THE CLIENT!!!"  # str
my_socket.send(str.encode(msg_1))  # codificar: str-->byte

receive_msg_2 = my_socket.recv(2048).decode("utf-8")
print(f"MSG: {receive_msg_2}")

my_socket.close()
