import socket
import termcolor


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return f"Connection to SERVER at ({self.ip}, {self.port})"

    def ping(self):
        print("OK!")

    def talk(self, msg):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((self.ip, self.port))

        my_socket.send(bytes(msg, "utf-8"))

        response = my_socket.recv(2048).decode("utf-8")

        my_socket.close()

        return response

    def debug_talk(self, msg):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((self.ip, self.port))

        my_socket.send(bytes(msg, "utf-8"))

        termcolor.cprint(f"To Server: {msg}", 'blue')

        response = my_socket.recv(2048).decode("utf-8")

        termcolor.cprint(f"From Server: {response}", 'green')

        my_socket.close()

        return response
