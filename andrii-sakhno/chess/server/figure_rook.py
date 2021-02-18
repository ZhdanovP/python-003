"""Figure module - rook"""

from figure import Figure, FT_ROOK


class FigureRook(Figure):
    """The class for rook"""
    def __init__(self, color=""):
        super().__init__(FT_ROOK, color)
        __slots__ = ()

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the rook rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The rook moves only on horizontal or vertical lines
        if start_x == finish_x or start_y == finish_y:
            return True

        return False
