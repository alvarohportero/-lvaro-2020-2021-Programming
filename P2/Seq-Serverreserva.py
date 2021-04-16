import socket
import server_utils

list_sequences =["ajajajjaja", "ebwsdffhjw", "alo", "svcjgb", "yatra"]

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
count_connections = 0
client_address_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        count_connections += 1
        # -- Server stopped manually
        client_address_list.append(cs, client_ip_port)
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()


    msg_raw = cs.recv(2048)
    print(msg_raw)
     # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()
    formatted_message = server_utils.format_command(msg)
    formatted_message = formatted_message.split(" ")
    if len(formatted_message) == 1:
        command = formatted_message[0]
    else:
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

