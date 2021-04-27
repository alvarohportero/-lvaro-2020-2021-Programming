import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

HTML_ASSETS = "html/"


def read_html_file(filename):
    return Path(filename).read_text()


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_get(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the clinet
        # info/C.html --> works as the file is in ./html/info/C.html
        # index.html ---> work as the file is in ./html/index.html
        # /info/index.html ---> error because the file index.html i not found there
        if self.path == "/":

            contents = read_html_file(".html/index.html")

        elif self.path == "/infoA/":
            contents = read_html_file("./html/info/A.html")
        elif self.path == "/infoC/":
            contents = read_html_file("./html/info/C.html")
        elif self.path == "/infoT/":
            contents = read_html_file("./html/info/T.html")
        elif self.path == "/infoG/":
            contents = read_html_file("./html/info/G.html")
        elif self.path.endswith(".html"):
            try:
                contents = read_html_file("./html" + self.path)
            except FileNotFoundError:
                contents = read_html_file("./html.error")
        else:
            contents = read_html_file("./html.error.html")

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
