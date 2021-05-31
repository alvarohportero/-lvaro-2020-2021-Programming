import socket
import termcolor
from FINAL_REVISION_seq import Seq

IP = "127.0.0.1"
PORT = 8080

SEQUENCES_LIST = [Seq("ACGT"),
                  Seq("ACGTACGT"),
                  Seq("ACGTACGTACGT"),
                  Seq("ACGTACGTACGTACGT"),
                  Seq("ACGTACGTACGTACGTACGT")]  # Comment: str

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
termcolor.cprint("SEQ Server configured!", 'white')

while True:
    termcolor.cprint(f"Waiting for clients...", 'white')

    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        termcolor.cprint("Server stopped by the user", 'white')
        ls.close()
        exit()
    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        # print(f"Message received: {msg}")
        if msg == "PING":
            termcolor.cprint(f"PING command!", 'green')
            response = "OK!\n"
            cs.send(response.encode())
            cs.close()
            termcolor.cprint(f"{response}", 'white')
        elif msg.startswith("GET"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "GET":
                try:
                    n = int(slices[1])
                    if 0 <= n <= len(SEQUENCES_LIST):
                        termcolor.cprint(f"GET", 'green')
                        seq = SEQUENCES_LIST[n]
                        termcolor.cprint(f"{seq}\n", 'white')
                        cs.send(f"{seq}".encode())
                        cs.close()
                except ValueError:
                    pass
        elif msg.startswith("INFO"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "INFO":
                termcolor.cprint(f"INFO", 'green')
                seq = Seq(slices[1])
                info = seq.info()
                termcolor.cprint(f"{info}", 'white')
                cs.send(f"{info}".encode())
                cs.close()
        elif msg.startswith("COMP"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "COMP":
                termcolor.cprint(f"COMP", 'green')
                seq = Seq(slices[1])
                comp = seq.complement()
                termcolor.cprint(f"{comp}\n", 'white')
                cs.send(f"{comp}\n".encode())
                cs.close()
        elif msg.startswith("REV"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "REV":
                termcolor.cprint(f"REV", 'green')
                seq = Seq(slices[1])
                rev = seq.reverse()
                termcolor.cprint(f"{rev}\n", 'white')
                cs.send(f"{rev}\n".encode())
                cs.close()
        elif msg.startswith("GENE"):
            slices = msg.split(" ")
            if len(slices) == 2 and slices[0] == "GENE":
                termcolor.cprint(f"GENE", 'green')
                filename = f"{slices[1]}.txt"
                seq = Seq()
                seq.read_fasta(filename)  # Comment: try-except
                termcolor.cprint(f"{seq}\n", 'white')
                cs.send(f"{seq}\n".encode())
                cs.close()
