"""
Contains a `NaiveHttpHandler` class and starts a `HTTPServer` with this handler
when started as a script.
"""
import os
from os.path import abspath, basename, dirname, join
import shutil
from http.server import SimpleHTTPRequestHandler, HTTPServer


class NaiveHttpHandler(SimpleHTTPRequestHandler):
    """A very simple HTTP handler to download a given file to a client."""
    def do_GET(self):
        file_to_download = "{}".format(self.path)
        file_name = basename(file_to_download)
        this_dir = dirname(abspath(__file__))
        pathname = join(this_dir, file_name)

        with open(pathname, 'rb') as file:
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Disposition", 'attachment; filename="{}"'.format(file_name))
            fs = os.fstat(file.fileno())
            self.send_header("Content-Length", str(fs.st_size))
            self.end_headers()
            shutil.copyfileobj(file, self.wfile)


httpd = HTTPServer(('localhost', 2828), NaiveHttpHandler)
httpd.serve_forever()
