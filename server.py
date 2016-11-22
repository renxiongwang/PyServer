import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	'''Deal with request and return'''
	#Page Pattern
	Page = '''\
		<html>
		<body>
		<p>Hello, Web!</p?
		</body>
		</html>
	'''
	# Deal with a GET request
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-Tyle", "text/html")
		self.send_header("Content-Length", str(len(self.Page)))
		self.end_headers()
		self.wfile.write(self.Page)

if __name__ == '__main__':
	serverAddress = ('', 8080)
	server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
	server.serve_forever()
