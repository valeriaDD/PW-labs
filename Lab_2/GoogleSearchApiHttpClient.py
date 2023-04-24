import socket
import ssl


class GoogleSearchApiHttpClient:
    def __init__(self):
        self.API_KEY = 'AIzaSyCTqdXi8_Xy2U_4zz_L78EktXdcxoDNnh0'
        self.CX = '067576e16e8364e9f'
        self.host = 'www.googleapis.com'
        self.port = 443
        self.context = ssl.create_default_context()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s = self.context.wrap_socket(self.s, server_hostname=self.host)

        self.s.connect((self.host, self.port))

    def send(self, query):
        request = f'GET /customsearch/v1?key={self.API_KEY}&cx={self.CX}&q="{query}""&num=10 HTTP/1.1\r\nHost: {self.host}\r\n\r\n'
        print(f"Sending request to {request.encode()}")

        self.s.send(request.encode())

        response = b""
        while True:
            data = self.s.recv()
            if not data:
                break
            response += data

        return response.decode('utf-8')

    def close_connection(self):
        self.s.close()
