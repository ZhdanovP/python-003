from ChessPiece import ChessPiece


class Rook(ChessPiece):
    """Class for Rook"""
    __slots__ = ()

    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

    def step(self, dest_x, dest_y):
        if self.pos_x == dest_x or self.pos_y == dest_y:
            self.pos_x = dest_x
            self.pos_y = dest_y
            return True
        else:
            return False
