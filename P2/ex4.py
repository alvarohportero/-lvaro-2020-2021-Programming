from Hello.Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"--------| {PRACTICE}, Exercise {EXERCISE} |-------")

IP = "127.0.0.1"
PORT = 9999
c = Client(IP, PORT)
print("Response", c.debug_talk("This is some message random from exercise 3"))

#NOTE: MY LAPTOP DOESNT ALLOW ME TO INSTALL THE TERMCOLOR, SO I HAVE COMMENTED ALL THAT PART, THATS THE REASON WHY WE MAY FIND SOME ERRORS.
