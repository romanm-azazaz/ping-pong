from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print(f"Request headers:\n{self.headers}")
        if validating_a_request(self.path): self.wfile.write(bytes("pong\n", "utf-8"))
        else: self.wfile.write(bytes('Please, send me a "ping", I will answer you "pong"\n', "utf-8"))

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--server_address', default=False, 
                        help='server_address')
    parser.add_argument('-p', '--server_port', default=False, 
                        help='server_port')
    script_arg = parser.parse_args()
    return script_arg

def validating_a_request(path):
    if path == "/ping":
        return True
    else: 
        return False

script_arg = create_parser()
address_server = script_arg.server_address or "localhost"
server_port = int(script_arg.server_port) or 8080

if __name__ == "__main__":        
    webServer = HTTPServer((address_server, server_port), MyServer)
    print(f"Server started http://{address_server}:{server_port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")