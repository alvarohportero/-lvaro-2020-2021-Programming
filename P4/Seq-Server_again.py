import socket
import termcolor
from seq import Seq

PORT = 8080
IP = "127.0.0.1"

SEQUENCES_LISTS = [Seq("ATTATATTA"),
                   Seq("CATCATGAT")]
                   Seq("TTTTTTT")
                   Seq("CCC")
                   Seq("TGGGTGGG")]

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
termcolor.cprint("The server is configured!", "white")
while True:
    # -- Waits for a client to connect
    termcolor.cprint("Waiting for Clients to connect", "white")

    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        termcolor.cprint("Server stopped by the user","white")
        ls.close()
        exit()
    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        #print(f"Message received:{msg})
        if msg =="PING":
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
                    if 0 <= n <= len (SEQUENCES_LISTS)
                        termcolor.cprint("GET","green")
                        seq = SEQUENCES_LISTS[n]
                        termcolor.cprint(f)


        formatted_message = server_utils.format_command(msg)
        formatted_message = formatted_message.split(" ")
        if len(formatted_message) == 1:
            command = formatted_message[0]
        command = formatted_message[0]
        argument = formatted_message[1]
    if command == "PING":
        server_utils.ping()
        # -- Send a response message to the client
        response = "OK!"
        cs.send(str(response).encode())
        # -- Close the data socket
    elif command == "GET":
        server_utils.print_colored("GET", "yellow")
        response = list_sequences[int(argument)]
        print(response)
        cs.send((response.encode()))
    else:
        response = "Not available command"
        cs.send(str(response).encode())
    cs.close()

