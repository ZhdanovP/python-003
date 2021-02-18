"""Chess server"""
import socket

from board import ChessBoard, GT_CHESS, GT_CHECKERS

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

board = ChessBoard()
board.new_game()

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        connection.sendall(board.bord_draw().encode())
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1000)
            print(data.decode())
            _, error_test = board.make_move(data.decode())
            connection.sendall((error_test + '\n' + board.bord_draw()).encode())

    finally:
        # Clean up the connection
        connection.close()
