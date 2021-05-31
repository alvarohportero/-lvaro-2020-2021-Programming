import socket
import termcolor


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return f"Connection to server at ({self.ip}, port : {self.port})"

    def ping(self):
        print("Ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up")
            s.close()
        except ConnectionRefusedError:
            print("Couldn't connect to the server. Is it running? HAve you check the ip and port?")

    def talk(self, msg):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((self.ip, self.port))
        print("To server:", msg)
        my_socket.send(bytes(msg, "utf-8"))
        response = my_socket.recv(2048).decode("utf-8")
        my_socket.close()
        return f"From server : {response}"

    def debug_talk(self, msg, ):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((self.ip, self.port))
        my_socket.send(bytes(msg, "utf-8"))
        termcolor.cprint(f"To server:{msg}", "blue")
        response = my_socket.recv(2048).decode("utf-8")
        termcolor.cprint(f"From server:{response}", "green")
        my_socket.close()
        return f"From server : {response}"
        # result = colored.talk
        # termcolor.cprint(result, "green")"""
