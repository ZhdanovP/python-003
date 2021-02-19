"""Figure module - bishop"""

from figure import Figure, FT_BISHOP


class FigureBishop(Figure):
    """The class for bishop"""
    def __init__(self, color=""):
        super().__init__(FT_BISHOP, color)
        __slots__ = ()

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the bishop rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The bishop only moves diagonally
        if abs(start_x - finish_x) == abs(start_y - finish_y):
            return True

        return False
