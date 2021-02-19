"""Figure module - king"""

from figure import Figure, FT_KING


class FigureKing(Figure):
    """The class for king"""
    def __init__(self, color=""):
        super().__init__(FT_KING, color)
        __slots__ = ()

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the king rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The king can walk only one square along
        if abs(start_x - finish_x + start_y - finish_y) == 1:
            return True

        return False
