from ChessPiece import ChessPiece


class Queen(ChessPiece):
    """Class for Queen"""
    __slots__ = ()

    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

    def step(self, dest_x, dest_y):
        if abs(self.pos_x-dest_x) <= 1 and abs(self.pos_y-dest_y) <= 1 or self.pos_x == dest_x or self.pos_y == dest_y:
            self.pos_x = dest_x
            self.pos_y = dest_y
            return True
        else:
            return False
