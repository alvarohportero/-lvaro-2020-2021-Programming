from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"--------| {PRACTICE}, Exercise {EXERCISE} |-------")

IP = "127.0.0.1"
PORT = 9992
c = Client(IP, PORT)
c.advanced_ping()
c.ping()
print(f"IP: {c.ip}, {c.port}")