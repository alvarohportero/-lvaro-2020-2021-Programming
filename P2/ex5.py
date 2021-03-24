from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"--------| {PRACTICE}, Exercise {EXERCISE} |-------")

IP = "127.0.0.1"
PORT = 9992
c = Client(IP, PORT)
print(c.talk("Sending U5 gene to server..."))
print(c.talk(Path("U5.txt").read_text()))
