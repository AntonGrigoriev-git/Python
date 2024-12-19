from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

PORT = 8000
VOTES_FILE = 'votes.json'

if not os.path.exists(VOTES_FILE):
    with open(VOTES_FILE, 'w') as f:
        json.dump({'Cats': 0, 'Dogs': 0, 'Parrots': 0}, f)

class VotingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_html().encode())

        elif self.path == '/results':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            with open(VOTES_FILE, 'r') as f:
                data = json.load(f)
                self.wfile.write(json.dumps(data).encode())

        elif self.path == '/styles.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('styles.css', 'r') as f:
                self.wfile.write(f.read().encode())

        elif self.path == '/script.js':
            self.send_response(200)
            self.send_header('Content-type', 'application/javascript')
            self.end_headers()
            with open('script.js', 'r') as f:
                self.wfile.write(f.read().encode())

        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/vote':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            vote = json.loads(post_data)

            # Обновляем данные о голосовании
            with open(VOTES_FILE, 'r+') as f:
                data = json.load(f)
                data[vote['candidate']] += 1
                f.seek(0)
                json.dump(data, f)
                f.truncate()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Vote counted!')

        elif self.path == '/reset':
            # Сбрасываем данные о голосовании
            with open(VOTES_FILE, 'w') as f:
                json.dump({'Cats': 0, 'Dogs': 0, 'Parrots': 0}, f)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Votes reset!')

    def get_html(self):
        with open('votes.html', 'r') as f:
            return f.read()

def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, VotingHandler)
    print(f'Server started on http://localhost:{PORT}')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Exit')
    finally:
        httpd.server_close()

if __name__ == '__main__':
    run()