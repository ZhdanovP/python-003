"""Chess game, python implementation"""


class ChessPiece:
    """Superclass for all chess pieces."""

    image = None

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.image[0 if self.color == Color.WHITE else 1]

    def step(self):
        pass

    def get_available_moves(self, board, x, y):
        moves = []
        if self.color == Color.BLACK and y < 7 and \
                board.get_color(x, y + 1) == Color.EMPTY:
            moves.append([x, y + 1])
        return moves


class Color:
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Empty:
    color = Color.EMPTY

    def get_available_moves(self, board, x, y):
        """Raise exception when there is no figure on passed coordinates"""
        raise Exception('No piece on this position -x:{}, y:{}'.format(x, y))

    def __str__(self):
        return ' # '


class Queen(ChessPiece):
    """Queen class implementation. The Queen can move as many squares, in any
    single direction, as long there is no piece blocks that path."""
    image = (' ♕ ', ' ♛ ')


class Rook(ChessPiece):
    """Rook class implementation. The rook can move as many squares, forwards,
    backwards, or sideways, as long as there is no piece blocking that path."""
    image = (' ♖ ', ' ♜ ')


class Bishop(ChessPiece):
    """Bishop class implementation. The bishop can move as many squares, in a
    diagonal path, as long as there is no piece blocks that path."""
    image = (' ♗ ', ' ♝ ')


class Knight(ChessPiece):
    """Knight class implementation. The knight can move two squares in one
    direction, then one square at a 90 degree angle to that second square.
    Unlike other pieces, the Knight can jump other pieces that are in it's
    path."""
    image = (' ♘ ', ' ♞ ')


class Pawn(ChessPiece):
    """Pawn class implementation. The pawn can move forward one square.
    It can only attack the square that is in the forward-diagonal position
    to it's location.
    If a pawn encounters a piece in the square in front of it, it can no longer
     move.On a pawns first move, it can move two squares forwards instead of
     one, as long as it does not inferior with the previous rule."""
    image = (' ♙ ', ' ♟ ')


class King(ChessPiece):
    """King class docstring. The King can move one square in any direction"""
    image = (' ♔ ', ' ♚ ')


class Board:
    def __init__(self):
        self.board = [[Empty()] * 8 for i in range(8)]

        for i in range(8):
            self.board[1][i] = Pawn(Color.BLACK)
            self.board[6][i] = Pawn(Color.WHITE)

        for k in range(0, 8, 7):
            try:
                self.board[0][k] = Rook(Color.BLACK)
                self.board[7][k] = Rook(Color.WHITE)
                self.board[0][k - 2], self.board[7][k - 2] = Bishop(
                    Color.BLACK), Bishop(Color.WHITE)
                self.board[0][k + 2], self.board[7][k + 2] = Bishop(
                    Color.BLACK), Bishop(Color.WHITE)
                self.board[0][k - 1], self.board[7][k - 1] = Knight(
                    Color.BLACK), Knight(Color.WHITE)
                self.board[0][k + 1], self.board[7][k+1] = Knight(
                    Color.BLACK), Knight(Color.WHITE)
                self.board[0][k + 3], self.board[7][k + 3] = Queen(
                    Color.BLACK), Queen(Color.WHITE)
                self.board[0][k + 4], self.board[7][k + 4] = King(
                    Color.BLACK), King(Color.WHITE)
            except:
                continue

    def get_color(self, x, y):
        return self.board[y][x].color

    def get_available_moves(self, x, y):
        return self.board[y][x].get_available_moves(self, x, y)

    def step(self, xy_from, xy_to):
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def __repr__(self):
        res = ''
        for i in range(8):
            res += ''.join(map(str, self.board[i])) + '\n'
        return res


b = Board()
print('Start position of the pieces on the board')
print(b)
moves = b.get_available_moves(x=2, y=1)
print('Available moves for Pawn - ', moves)
b.step([2, 1], moves[0])
print('Position of the pieces on the board after 1st move')
print(b)