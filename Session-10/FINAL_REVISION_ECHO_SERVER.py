import socket

PORT = 8080
IP = "localhost"  # IP local por defecto
MAX_OPEN_REQUESTS = 5
number_con = 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen(MAX_OPEN_REQUESTS)

    print(f"Waiting for connections at ({IP}, {PORT})...")
    while True:
        (client_socket, address) = server_socket.accept()

        number_con += 1
        print(f"CONNECTION: {number_con}. Address: {address} | Socket: {client_socket}")

        b = client_socket.recv(2048)
        msg = b.decode("utf-8")  # Decodificar: bytes -> str
        print(f"MSG: {msg}")

        msg = "HELLO FROM THE SERVER!!!"  # str
        client_socket.send(str.encode(msg))  # Codificar: str -> bytes

        client_socket.close()
except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))
except KeyboardInterrupt:
    print("Server stopped by t he user")
    server_socket.close()
