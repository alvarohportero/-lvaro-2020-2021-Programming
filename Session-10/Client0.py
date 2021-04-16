import socket
#import termcolor

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

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

    def __str__(self):
        return f"Connection to server at {self.ip}, port : {self.port}"

    def talk(self, msg):
        #colorama.init(strip="False")
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        #print(termcolor.colored("To server", "yellow"))
        print("To server:", msg)
        s.send(msg.encode())
        # Receive data
        response = s.recv(2048).decode("utf-8")
        print("From server", response)
        # Close the socket
        s.close()
        # Return the response
        return f"From server : {response}"

    """def debug_talk(self, colored):
        result = colored.talk
        termcolor.cprint(green, result)"""
