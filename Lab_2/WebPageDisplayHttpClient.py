import re
import ssl
import socket
from urllib.parse import urlparse


class WebPageDisplayHttpClient:
    port = 443

    def send(self, url):
        if self.is_valid_url(url):
            host, path = self.parse_url(url)

            context = ssl.create_default_context()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s = context.wrap_socket(s, server_hostname=host)

            s.connect((host, self.port))

            request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
            s.sendall(request.encode())

            response = b""
            while True:
                data = s.recv()
                if not data:
                    break
                response += data

            response = response.decode('utf-8')
            status_code = int(response.split()[1])

            if 300 <= status_code < 400:
                new_url = response.split('\r\n')[1].split(' ')[1]
                return self.send(new_url)

            s.close()
            return response
        else:
            print("Invalid url")
            return ""

    @staticmethod
    def is_valid_url(url):
        url_regex = re.compile(
            r"^(?:http|ftp)s?://"  # scheme
            r"(?:\S+(?::\S*)?@)?(?:\S+\.)+\S{2,}"  # netloc
            r"(?:/\S*)?"  # path
            r"(?:\?\S*)?"  # query string
            r"(?:#\S*)?$"  # fragment
            , re.IGNORECASE
        )

        return url_regex.match(url)

    @staticmethod
    def parse_url(url):
        parsed = urlparse(url)

        return parsed.netloc, parsed.path