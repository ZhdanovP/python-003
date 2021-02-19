# This sample receive from https://pymotw.com/3/socket/tcp.html
import socket
import sys

# Create a TCP/IP socket
"""
AF_INET is an address family that is used to designate the type of addresses 
that your socket can communicate with (in this case, Internet Protocol v4 addresses).
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data == b'GET:data.txt':
                print('sending file to the client')
                file_data = ""
                with open("data.txt", "r") as f:
                    for x in f:
                        file_data = file_data + x
                print(file_data)
                bf_data = bytes(file_data, 'ascii')
                connection.sendall(bf_data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()