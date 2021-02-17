import random
from abc import ABC, abstractmethod
"""The module "chess" implements the game of chess in the console"""

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

# Board size
BOARD_SIZE = 8

# Horizontal letters
LETTER_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


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


# TODO: implement first move for 2 cell
# TODO: implement correct beat
class FigurePawn(Figure):
    """The class for pawn"""
    def __init__(self, color=""):
        super().__init__(FT_PAWN, color)

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


class FigureRook(Figure):
    """The class for rook"""
    def __init__(self, color=""):
        super().__init__(FT_ROOK, color)

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the rook rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The rook moves only on horizontal or vertical lines
        if start_x == finish_x or start_y == finish_y:
            return True

        return False


class FigureKnight(Figure):
    """The class for knight"""
    def __init__(self, color=""):
        super().__init__(FT_KNIGHT, color)

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the knight rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The knight can move two (three) squares in a straight line and three (two) squares to the side.
        if (abs(start_x - finish_x) == 1 and abs(start_y - finish_y) == 2) or \
                (abs(start_x - finish_x) == 2 and abs(start_y - finish_y) == 1):
            return True

        return False


class FigureBishop(Figure):
    """The class for bishop"""
    def __init__(self, color=""):
        super().__init__(FT_BISHOP, color)

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the bishop rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The bishop only moves diagonally
        if abs(start_x - finish_x) == abs(start_y - finish_y):
            return True

        return False


class FigureQueen(Figure):
    """The class for queen"""
    def __init__(self, color=""):
        super().__init__(FT_QUEEN, color)

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


class FigureKing(Figure):
    """The class for king"""
    def __init__(self, color=""):
        super().__init__(FT_KING, color)

    def check_step(self, start_x, start_y, finish_x, finish_y):
        """The function returns True if the move satisfies the king rules"""
        if not super()._check_for_skip_move(start_x, start_y, finish_x, finish_y):
            return False

        # The king can walk only one square along
        if abs(start_x - finish_x + start_y - finish_y) == 1:
            return True

        return False


class ChessBoard:
    """Class for chess board with players"""
    def __init__(self):
        __slots__ = ("_whiteTurn", "_board")
        self._whiteTurn = True
        self._board = [[0] * BOARD_SIZE for i in range(BOARD_SIZE)]

    def new_game(self):
        """The function creates a new game and randomly places the figures"""
        # place figures for each color
        for color in [PC_WHITE, PC_BLACK]:
            # place pawns not in 1 or 8 row
            for pawnCount in range(0, BOARD_SIZE):
                self._random_place_figure_on_bord(FigurePawn(color))

            # place rooks figures
            self._random_place_figure_on_bord(FigureRook(color))
            self._random_place_figure_on_bord(FigureRook(color))

            # place knights figures
            self._random_place_figure_on_bord(FigureKnight(color))
            self._random_place_figure_on_bord(FigureKnight(color))

            # place bishop figures
            # TODO: first bishop should be in the black cell, second in the white cell
            self._random_place_figure_on_bord(FigureBishop(color))
            self._random_place_figure_on_bord(FigureBishop(color))

            # place queen figure
            self._random_place_figure_on_bord(FigureQueen(color))

            # place king figures
            self._random_place_figure_on_bord(FigureKing(color))

    def bord_draw(self):
        """The function redraws the position of the figures"""
        # for i in self.player_white.figures:
        print("   A  B  C  D  E  F  G  H")
        # print("   1  2  3  4  5  6  7  8")
        print("  -------------------------")

        i = 0
        for x in self._board:
            row = ""
            for y in x:
                row += '|' + ("  " if y == 0 else y.symbol())

            i += 1
            print(f'{i}', row + "|")
            print("  -------------------------")

        print("")
        print(("White" if self._whiteTurn else "Black") + " turn")

    def make_move(self, start_position, finish_position):
        """The function processes the move"""
        # converting raw position
        start_x, start_y = self._convert_raw_position(start_position)
        if start_y == -1:
            self._show_error("Wrong start position")
            return False

        finish_x, finish_y = self._convert_raw_position(finish_position)
        if finish_y == -1:
            self._show_error("Wrong finish position")
            return False

        # trying to find a figure
        cur_figure = self._figure_find(start_x, start_y)
        if cur_figure == 0:
            self._show_error("Figure not found!")
            return False

        # check that the figure is the correct color
        if self._whiteTurn and cur_figure.is_black():
            self._show_error("Please move white figure")
            return False

        if not self._whiteTurn and cur_figure.is_white():
            self._show_error("Please move black figure")
            return False

        # check that the figure's move is correct
        if not cur_figure.check_step(start_x, start_y, finish_x, finish_y):
            self._show_error("This figure cannot walk like that ")
            return False

        # check the absence of obstacles
        # TODO: implement check for obstacles

        # check the correctness of the final position
        if not self._check_target(finish_x, finish_y):
            return False

        # beat the opponent's figure
        # move the figure
        self._move_figure_to(cur_figure, start_x, start_y, finish_x, finish_y)

        self._whiteTurn = not self._whiteTurn

    def _random_place_figure_on_bord(self, figure):
        """Function for placing a figure in a random cell """
        # pawn can't place in first and last horizontal line
        indent = (1 if figure.figure_type() == FT_PAWN else 0)

        while True:
            pos_x = random.randint(indent, BOARD_SIZE-1-indent)
            pos_y = random.randint(0, BOARD_SIZE-1)
            if not self._figure_find(pos_x, pos_y):
                self._board[pos_x][pos_y] = figure
                break

    def _figure_find(self, pos_x, pos_y):
        """Function for finding a figure by coordinates"""
        return self._board[pos_x][pos_y]

    def _check_target(self, finish_x, finish_y):
        """Function for checking the target cell"""
        target_figure = self._figure_find(finish_x, finish_y)

        # cell is free
        if target_figure == 0:
            return True

        # It is forbidden to beat own figures
        if target_figure.is_white() == self._whiteTurn:
            self._show_error("You can't beat your own figures")
            return False

        # It is forbidden to beat own figures
        if target_figure.figure_type() == FT_KING:
            self._show_error("You can't beat the king")
            return False

        return True

    @staticmethod
    def _convert_raw_position(raw_position):
        """Function to check and convert cell name to coordinates"""
        if len(raw_position) != 2:
            return '', -1

        if raw_position[0].upper() not in LETTER_LIST:
            return '', -1

        if not raw_position[1].isdigit() or int(raw_position[1]) not in range(1, BOARD_SIZE+1):
            return '', -1

        return int(raw_position[1])-1, LETTER_LIST.index(raw_position[0].upper())

    def _move_figure_to(self, figure, start_x, start_y, finish_x, finish_y):
        self._board[finish_x][finish_y] = figure
        self._board[start_x][start_y] = 0

    @staticmethod
    def _show_error(error_text):
        print("")
        print('*'*(len(error_text)+4))
        print("* " + error_text + " *")
        print('*' * (len(error_text)+4))
        print("")


if __name__ == "__main__":
    board = ChessBoard()

    board.new_game()
    print("Enter 'q' to close chess")

    while True:
        print("=======================================================================================================")
        print("")
        board.bord_draw()
        print("")
        position_start = input("Please type figure start position to move (example 'a1 or 'g7): ")
        if position_start.lower() == 'q':
            exit()

        position_finish = input("Please type figure finish position to move (example 'a1 or 'g7): ")
        if position_finish.lower() == 'q':
            exit()

        board.make_move(position_start, position_finish)
