"""Chess board module"""

# from chess.server.figure import FT_PAWN, FT_KING, PC_BLACK, PC_WHITE
# from chess.server.figure_pawn import FigurePawn
# from chess.server.figure_rook import FigureRook
# from chess.server.figure_knight import FigureKnight
# from chess.server.figure_bishop import FigureBishop
# from chess.server.figure_queen import FigureQueen
# from chess.server.figure_king import FigureKing

from figure import FT_PAWN, FT_KING, PC_BLACK, PC_WHITE
from figure_pawn import FigurePawn
from figure_rook import FigureRook
from figure_knight import FigureKnight
from figure_bishop import FigureBishop
from figure_queen import FigureQueen
from figure_king import FigureKing

import random

# Board size
BOARD_SIZE = 8

# Game type
GT_CHESS = 0
GT_CHECKERS = 1

# Horizontal letters
LETTER_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


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
        scene  = "  A  B  C  D  E  F  G  H\\n"
        scene += " -------------------------\\n"

        i = 0
        for x in self._board:
            row = ""
            for y in x:
                row += '|' + ("  " if y == 0 else y.symbol())

            i += 1
            scene += f'{i}' + row + "|\\n"
            scene += " -------------------------\\n"

        scene += '\\n' + ("White" if self._whiteTurn else "Black") + " turn" + '\\n'

        return scene

    def make_move(self, raw_position):
        """The function processes the move"""
        # converting raw position
        start_x, start_y, finish_x, finish_y = self._convert_raw_position(raw_position)
        if start_x is None:
            return False, self._show_error("Wrong move data")

        # trying to find a figure
        cur_figure = self._figure_find(start_x, start_y)
        if cur_figure == 0:
            return False, self._show_error("Figure not found!")

        # check that the figure is the correct color
        if self._whiteTurn and cur_figure.is_black():
            return False, self._show_error("Please move white figure")

        if not self._whiteTurn and cur_figure.is_white():
            return False, self._show_error("Please move black figure")

        # check that the figure's move is correct
        if not cur_figure.check_step(start_x, start_y, finish_x, finish_y):
            return False, self._show_error("This figure cannot walk like that ")

        # check the absence of obstacles
        # TODO: implement check for obstacles

        # check the correctness of the final position
        is_no_error, error_text = self._check_target(finish_x, finish_y)
        if not is_no_error:
            return False, ""

        # beat the opponent's figure
        # move the figure
        self._move_figure_to(cur_figure, start_x, start_y, finish_x, finish_y)

        self._whiteTurn = not self._whiteTurn
        return True, ""

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
            return True, ""

        # It is forbidden to beat own figures
        if target_figure.is_white() == self._whiteTurn:
            return False, self._show_error("You can't beat your own figures")

        # It is forbidden to beat own figures
        if target_figure.figure_type() == FT_KING:
            return False, self._show_error("You can't beat the king")

        return True

    @staticmethod
    def _convert_raw_position(raw_position):
        """Function to check and convert cell name to coordinates"""
        if len(raw_position) != 5:
            return None, None, None, None

        start_x = raw_position[0]
        start_y = raw_position[1]
        finish_x = raw_position[3]
        finish_y = raw_position[4]

        # checked data type
        if not start_x.isalpha() or not finish_x.isalpha() or not start_y.isdigit() or not finish_y.isdigit():
            print("type error")
            return None, None, None, None

        start_y = int(start_y)-1
        finish_y = int(finish_y)-1

        # checked valid x position
        if start_x.upper() not in LETTER_LIST or finish_x.upper() not in LETTER_LIST:
            print("valid x error")
            return None, None, None, None

        # checked valid y position
        if start_y not in range(0, BOARD_SIZE) or finish_y not in range(0, BOARD_SIZE):
            print("valid y error", start_y, finish_y)
            return None, None, None, None

        return start_y, LETTER_LIST.index(start_x.upper()), finish_y, LETTER_LIST.index(finish_x.upper())

    def _move_figure_to(self, figure, start_x, start_y, finish_x, finish_y):
        """Function to move figure from start to finish position"""
        self._board[finish_x][finish_y] = figure
        self._board[start_x][start_y] = 0

    @staticmethod
    def _show_error(error_text):
        """Function to show formatted error"""
        return "\n{}\n* {} *\n{}\n ".format('*'*(len(error_text)+4), error_text, '*' * (len(error_text)+4))
