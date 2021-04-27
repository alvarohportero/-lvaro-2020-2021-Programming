import socket
import termcolor
import pathlib
from urllib.parse import urlparse, parse_qs

IP = "127.0.0.1"
PORT = 8080
HTML_ASSETS = "./html/"


def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()
    # print(req)
    print("Message FROM CLIENT: ")

    lines = req.split('\n')

    # The request line is the first
    req_line = lines[0]
    request = req_line.split(" ")[1]
    path_name = request.split("?")[0]
    try:
        o = urlparse(req_line.split(" ")[1])
        query = parse_qs(o.query)
        print(o)
        print(query)

    except IndexError:
        pass
    print("Resource requested:", path_name)

    termcolor.cprint(req_line, "green")
    # This new contents are written in HTML language
    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"
    # we could include the filenotofounderror
    if path_name == "/":
        body = read_html_file(HTML_ASSETS + "index.html")
    elif path_name == "/info/A":
        body = read_html_file(HTML_ASSETS + "A.html")
    elif path_name == "/info/C":
        body = read_html_file(HTML_ASSETS + "C.html")
    elif path_name == "/info/T":
        body = read_html_file(HTML_ASSETS + "T.html")
    elif path_name == "/info/G":
        body = read_html_file(HTML_ASSETS + "G.html")
    else:
        body = read_html_file((HTML_ASSETS + "error.html"))

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("SEQ Server configured!")
# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()
