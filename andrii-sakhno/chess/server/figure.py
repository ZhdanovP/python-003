"""Base figure module"""

from abc import ABC, abstractmethod

# Figure type
FT_PAWN = "p"
FT_ROOK = "R"
FT_KNIGHT = "N"
FT_BISHOP = "B"
FT_QUEEN = "Q"
FT_KING = "K"

# Player color
PC_WHITE = "w"
PC_BLACK = "b"


class Figure(ABC):
    """Base class for figure"""
    def __init__(self, figure_type="", color=""):
        __slots__ = ("_figure_type", "_color")
        self._figure_type = figure_type
        self._color = color

    def figure_type(self):
        """The function returns type of figure"""
        return self._figure_type

    def is_white(self):
        """The function returns True if figure is white"""
        return self._color == PC_WHITE

    def is_black(self):
        """The function returns True if figure is black"""
        return self._color == PC_BLACK

    def symbol(self):
        """The function returns the graphic symbol of the figure"""
        return self._color + self._figure_type

    @staticmethod
    def _check_for_skip_move(start_x, start_y, finish_x, finish_y):
        """The function returns the True if the move satisfies the common rules"""
        # check for skip turn
        if start_x != finish_x or start_y != finish_y:
            return True
        return False

    @abstractmethod
    def check_step(self, start_x, start_y, finish_x, finish_y):
        """Interface function for checking move capability"""
        pass
