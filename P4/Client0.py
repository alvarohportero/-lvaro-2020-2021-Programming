import socket
import termcolor


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return f"Connection to server at {self.ip}, port : {self.port}"

    def ping(self):
        print("Ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up")
            s.close()
        except ConnectionRefusedError:
            print("Couldnt connect to the server. Is it running? HAve you check the ip and port?")

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To server:", msg)
        s.send(bytes(msg, "utf-8"))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return f"From server : {response}"

    def debug_talk(self, msg, ):
        dt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dt.connect((self.ip, self.port))
        dt.send(bytes(msg, "utf-8"))
        termcolor.cprint(f"To server:{msg}", "blue")
        response = dt.recv(2048).decode("utf-8")
        termcolor.cprint(f"From server:{response}", "green")
        dt.close()
        return f"From server : {response}"
        # result = colored.talk
        # termcolor.cprint(result, "green")"""
