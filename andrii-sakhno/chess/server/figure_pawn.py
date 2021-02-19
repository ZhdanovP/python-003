"""Figure module - pawn"""

from figure import Figure, FT_PAWN


# TODO: implement first move for 2 cell
# TODO: implement correct beat
class FigurePawn(Figure):
    """The class for pawn"""
    def __init__(self, color=""):
        super().__init__(FT_PAWN, color)
        __slots__ = ()

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the pawn rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The pawn rook moves only one square along the vertical line.
        if self.is_white() and start_x - finish_x == 1:
            return True

        if self.is_black() and start_x - finish_x == -1:
            return True

        return False
