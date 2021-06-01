import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
import server_utils as su
from seq import Seq


IP = "127.0.0.1"
PORT = 8080
SEQUENCES_LISTS = [Seq("ATTATATTA"), Seq("CATCATGAT"), Seq("TTTTTTT"), Seq("CCC"), Seq("TGGGTGGG")]
LIST_GENES = ["ADA.txt", "FRAT1.txt", "FNX.txt", "RNU6_269P.txt"]


class MyWebServerRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.requestline, "green")
        print((self.path, "blue"))

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested:", path_name)
        print("Parameters:", arguments)

        context = {}
        if path_name == "/":
            context["n_sequences"] = len(SEQUENCES_LISTS)
            context["list_genes"] = LIST_GENES
            contents = su.read_template_html_file("./html/index.html").render(context=context)
        elif path_name == "/ping":
            contents = su.read_template_html_file("./html/ping.html").render()
        elif path_name == "/get":
            number_sequence = arguments["sequence"][0]
            contents = su.get(SEQUENCES_LISTS, number_sequence)
        elif path_name == "/gene":
            gene = arguments["gene"][0]
            contents = su.gene(gene)
        elif path_name == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["operation"][0]
            contents = su.operation(sequence,operation)

        else:
            contents = su.read_template_html_file("./html/error.html")

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')

        self.send_header("Content-Length", str(len(contents.encode())))

        self.end_headers()
        self.wfile.write(bytes(contents, "utf-8"))


handler = MyWebServerRequestHandler

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer((IP, PORT), handler) as httpd:  # HTTP Daemon
    print(f"Serving at port {PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped by the user")
