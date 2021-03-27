from Client0 import Client
from seq import Seq

PRACTICE = 2
EXERCISE = 7

print(f"--------| {PRACTICE}, Exercise {EXERCISE} |-------")

IP = "127.0.0.1"
PORT = 9992
PORT_2 = 9777
c = Client(IP, PORT)
c_2 = Client(IP, PORT_2)

s = Seq()
s.read_fasta_format("../P1/FRAT1.txt")
count = 0
i = 0
while i < len(s.bases) and count < 5:
    fragment = s.bases[i:i + 10]
    count += 1
    i += 10
    print(f"Fragment {count} : {fragment}")
    if count % 2 == 0:
        print(c_2.talk(f"Fragment {count} : {fragment}"))
    else:
        print(c.talk(f"Fragment {count} : {fragment}"))
