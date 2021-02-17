from ChessPiece import ChessPiece


class Knight(ChessPiece):
    """Class for Knight"""
    __slots__ = ()

    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

    def step(self, dest_x, dest_y):
        """Correct move - if difference between one coordinates is 1 AND
            between others is 2"""
        dx = abs(self.pos_x - dest_x)
        dy = abs(self.pos_y - dest_y)
        if dx == 1 and dy == 2 or dx == 2 and dy == 1:
            self.pos_x = dest_x
            self.pos_y = dest_y
            return True
        else:
            return False
