import socket

PORT = 9999
IP = ""  # IP LOCAL POR DEFECTO
MAX_OPEN_REQUESTS = 5  # cd para añadir carpeta    # python server.py para inicialiarlo por ejemplo

number_con = 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen(MAX_OPEN_REQUESTS)

    print(f"Waiting for connections at {IP}, {PORT} ...")
    while True:
        (client_socket, address) = server_socket.accept()

        number_con += 1
        print(f"CONNECTION: {number_con}. Address:{address} | Socket:{client_socket}")

        receive_msg_1 = client_socket.recv(2048).decode("utf-8")  # decodificar de bytes--->string
        print(f"MSG: {receive_msg_1}")

        message = "Hello from the teachers server"
        client_socket.send(message.encode())
        client_socket.close()
except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))
except KeyboardInterrupt:
    print("Server stopped by the user")
    server_socket.close()
