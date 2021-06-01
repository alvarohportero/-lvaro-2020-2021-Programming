import socket
import termcolor
from seq import Seq

PORT = 8080
IP = "127.0.0.1"

SEQUENCES_LISTS = [Seq("ATTATATTA"),
                   Seq("CATCATGAT"),
                   Seq("TTTTTTT"),
                   Seq("CCC"),
                   Seq("TGGGTGGG")]

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
termcolor.cprint("The server is configured!", "white")
while True:
    termcolor.cprint("Waiting for Clients to connect", "white")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        termcolor.cprint("Server stopped by the user", "white")
        ls.close()
        exit()
    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        # print(f"Message received:{msg})
        if msg == "PING":
            termcolor.cprint("PING command", "green")
            response = "OK!"
            cs.send(response.encode())
            cs.close()
            termcolor.cprint(f"{response}", "white")
        elif msg.startswith("GET"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "GET":
                try:
                    n = int(slices[1])
                    if 0 <= n <= len(SEQUENCES_LISTS):
                        termcolor.cprint("GET", "green")
                        seq = SEQUENCES_LISTS[n]
                        termcolor.cprint(f"{seq}\n", 'white')
                        cs.send(f"{seq}".encode())
                        cs.close()
                except ValueError:
                    pass
        elif msg.startswith("INFO"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "INFO":
                try:
                    n = int(slices[1])
                    if 0 <= n <= len(SEQUENCES_LISTS):
                        termcolor.cprint("INFO", "green")
                        seq = Seq(slices[1])
                        info = seq.info()
                        termcolor.cprint(f"{info}\n", 'white')
                        cs.send(f"{info}".encode())
                        cs.close()
                except ValueError:
                    pass
        elif msg.startswith("COMP"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "COMP":
                termcolor.cprint("COMP", "green")
                seq = Seq(slices[1])
                complement = seq.complementary()
                termcolor.cprint(f"{complement}\n", 'white')
                cs.send(f"{complement}".encode())
                cs.close()
        elif msg.startswith("REV"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "REV":
                termcolor.cprint("REV", "green")
                seq = Seq(slices[1])
                reversing = seq.reverse_mode()
                termcolor.cprint(f"{reversing}\n", 'white')
                cs.send(f"{reversing}".encode())
                cs.close()
        elif msg.startswith("GENE"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "GENE":
                termcolor.cprint("GENE", "green")
                file = f"{slices[1]}.txt"
                seq_gene = Seq
                seq_gene.read_fasta_format(file)
                termcolor.cprint(f"{seq_gene}\n", 'white')
                cs.send(f"{seq_gene}".encode())
                cs.close()
