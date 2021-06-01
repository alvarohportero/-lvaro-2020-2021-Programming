import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su
from pathlib import Path

PORT = 8080
ENDPOINTS = ["/", "/listSpecies", "/karyotype", "/chromosomeLength", "/geneSeq", "/geneInfo", "/geneCalc"]

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, "blue")

        url = urlparse(self.path)
        endpoint = url.path
        parameters = parse_qs(url.query)
        print("Endpoint: ", endpoint)
        print("Parameters: ", parameters)

        has_error = False
        contents = ""
        status = 400  # BAD_REQUEST
        if endpoint in ENDPOINTS:
            if endpoint == "/":
                status = 200
                contents = Path("./html/index.html").read_text()
            elif endpoint == "/listSpecies":
                if len(parameters) == 0:
                    status, contents = su.list_species()
                elif len(parameters) == 1:
                    try:
                        limit = int(parameters['limit'][0])
                        status, contents = su.list_species(limit)
                    except (KeyError, ValueError):
                        has_error = True
                else:
                    has_error = True
            elif endpoint == "/karyotype":
                if len(parameters) == 1:
                    try:
                        specie = parameters['specie'][0]
                        status, contents = su.karyotype(specie)
                    except (KeyError, ValueError):
                        has_error = True
                else:
                    has_error = True
            elif endpoint == "/chromosomeLength":
                if len(parameters) == 2:
                    try:
                        specie = parameters['specie'][0]
                        chromo = parameters['chromo'][0]
                        status, contents = su.chromosome_length(specie, chromo)
                    except (KeyError, ValueError):
                        has_error = True
                else:
                    has_error = True
            elif endpoint == "/geneSeq":
                if len(parameters) == 1:
                    try:
                        gene = parameters['gene'][0]
                        status, contents = su.gene_seq(gene)
                    except (KeyError, ValueError):
                        has_error = True
                else:
                    has_error = True
            elif endpoint == "/geneInfo":
                if len(parameters) == 1:
                    try:
                        gene = parameters['gene'][0]
                        status, contents = su.gene_info(gene)
                    except (KeyError, ValueError):
                        has_error = True
                else:
                    has_error = True
            elif endpoint == "/geneCalc":
                if len(parameters) == 1:
                    try:
                        gene = parameters['gene'][0]
                        status, contents = su.gene_calc(gene)
                    except (KeyError, ValueError):
                        has_error = True
                else:
                    has_error = True
        else:
            has_error = True

        if has_error:
            contents = Path("./html/error.html").read_text()

        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())
        print(contents)


handler = TestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
