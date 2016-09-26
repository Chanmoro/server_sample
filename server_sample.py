from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Custom Web serer class.
class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        print('[Request method] POST')
        print('[Request headers]\n' + str(self.headers))

        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len).decode('utf-8')
        print('[Request doby]\n' + post_body)

        # JSONデータを受け取る場合
        # received_data = json.loads(post_body)

        # レスポンス処理
        response_data = b'OK' # byte型にする必要がある
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=UTF-8')
        self.send_header('Content-length', len(response_data))
        self.end_headers()
        self.wfile.write(response_data)

# Start the server.
host = ''
port = 8881
httpd = HTTPServer((host, port), MyHTTPRequestHandler)

print('Server Starting...')
print('Listening at port :%d' % port)

try:
    httpd.serve_forever()
except:
    print('Server Stopped')
