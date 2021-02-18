"""Figure module - knight"""

from figure import Figure, FT_KNIGHT


class FigureKnight(Figure):
    """The class for knight"""
    def __init__(self, color=""):
        super().__init__(FT_KNIGHT, color)
        __slots__ = ()

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the knight rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The knight can move two (three) squares in a straight line and three (two) squares to the side.
        if (abs(start_x - finish_x) == 1 and abs(start_y - finish_y) == 2) or \
                (abs(start_x - finish_x) == 2 and abs(start_y - finish_y) == 1):
            return True

        return False
