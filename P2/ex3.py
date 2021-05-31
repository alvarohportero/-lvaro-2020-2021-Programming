from Hello.Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"--------| {PRACTICE}, Exercise {EXERCISE} |-------")

IP = "127.0.0.1"
PORT = 9999
c = Client(IP, PORT)
print("Response", c.talk("This is some message random from exercise 3"))
