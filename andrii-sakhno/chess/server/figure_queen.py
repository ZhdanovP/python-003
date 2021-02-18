"""Figure module - queen"""

from figure import Figure, FT_QUEEN


class FigureQueen(Figure):
    """The class for queen"""
    def __init__(self, color=""):
        super().__init__(FT_QUEEN, color)
        __slots__ = ()

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the queen rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The queen can walk like bishop
        if abs(start_x - finish_x) == abs(start_y - finish_y):
            return True

        # The queen can walk like bishop
        if start_x == finish_x or start_y == finish_y:
            return True

        return False
