import socket

PORT = 9992  # servidor
IP = "127.0.0.1"  # SERVIDOR

try:
    while True:
        message_1= input("Enter a message:")

        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        my_socket.connect((IP, PORT))  # ASOCIA A MI SOCKET LA IP LOCAL Y UN PUERTO LIBRE ALEATORIO


        my_socket.send(str.encode(message_1))  # codificar: str-->byte

        my_socket.close()
except KeyboardInterrupt:
    print("client stopped program")
