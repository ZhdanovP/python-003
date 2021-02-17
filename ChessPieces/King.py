from ChessPiece import ChessPiece


class King(ChessPiece):
    """Class for King"""
    __slots__ = ()

    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

    def step(self, dest_x, dest_y):
        if (self.pos_x - dest_x == 1 or self.pos_x - dest_x == -1 or self.pos_x - dest_x == 0) and \
                (self.pos_y - dest_y == 1 or self.pos_y - dest_y == -1 or self.pos_y - dest_y == 0):
            self.pos_x = dest_x
            self.pos_y = dest_y
            return True
        else:
            return False
