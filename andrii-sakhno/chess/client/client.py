"""Chess client"""

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to chess server (host = {} port = {})'.format(*server_address))
sock.connect(server_address)

try:
    data = sock.recv(10000)
    print(data.decode("unicode_escape"))
    while True:
        # Send data
        message = input("Please type figure start and finish position  to move (example 'a1-b2'): ").encode()
        print('sending {!r}'.format(message))
        sock.sendall(message)

        data = sock.recv(10000)
        print(data.decode("unicode_escape"))

finally:
    print('closing socket')
    sock.close()
