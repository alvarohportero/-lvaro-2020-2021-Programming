from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

print("-----| Practice 3|------")

c = Client(IP, PORT)
print(c)

print("* TesT of  PING...")
response = c.talk("PING")
print(response)

print("* Test of  GET...")
seq = c.talk("GET 0")
print(f"GET 0: {seq}")
response = c.talk("GET 1")
print(f"GET 1: {response}")
response = c.talk("GET 2")
print(f"GET 2: {response}")
response = c.talk("GET 3")
print(f"GET 3: {response}")
response = c.talk("GET 4")
print(f"GET 4: {response}")

print()

print("* Testing INFO...")
response = c.talk(f"INFO {seq}")
print(response)

print("* Test of  COMP...")
print(f"COMP {seq}")
response = c.talk(f"COMP {seq}")
print(response)

print("* Test of  REV...")
print(f"REV {seq}")
response = c.talk(f"REV {seq}")
print(response)

print("* Test of  GENE...")
print("GENE U5")
response = c.talk("GENE U5")
print(response)

print()

print("GENE ADA")
response = c.talk("GENE ADA")
print(response)

print()

print("GENE FRAT1")
response = c.talk("GENE FRAT1")
print(response)

print()

print("GENE FXN")
response = c.talk("GENE FXN")
print(response)

print()

print("GENE RNU6_269P")
response = c.talk("GENE RNU6_269P")
print(response)

print()