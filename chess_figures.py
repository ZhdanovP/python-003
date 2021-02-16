"""Module defines series of classes for all chess figures"""

import math
import random

X = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
Y = {1, 2, 3, 4, 5, 6, 7, 8}
COLOR_WHITE = 'WHITE'
COLOR_BLACK = 'BLACK'
COLOR = {COLOR_BLACK, COLOR_WHITE}


class OutOfBoard(Exception):
    pass


class InvalidMove(Exception):
    pass


class NoMove(Exception):
    pass


class ChessPoint:
    """Class defines chess point """
    x = None
    y = None
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}{}".format(self.x, self.y)


def inboard(step_to):
    """function to validate if point is within chess board defined by X an Y
    accept object: ChessPoint
    return: boolean"""
    if (step_to.x not in X) or (step_to.y not in Y):
        raise OutOfBoard
    return True


class Figure:
    """Class is a parent for all figures. It means to be inherited"""
    __current_point__ = None
    __color__ = None

    def __init__(self, color: COLOR, initial_point: ChessPoint):
        """constructor class Figure, initialise figures setup: setup point and color"""
        if not inboard(initial_point):
            raise OutOfBoard
        self.__color__ = color
        self.__current_point__ = initial_point

    def valid(self, step_to: ChessPoint):
        """ method validate if step to is valid for the particular figure.
        It must to be implemented for any specific figure"""
        raise NotImplementedError

    def horizontal(self, step_to: ChessPoint):
        """verifies if figure is going horizontal"""
        if self.__current_point__.y == step_to.y:
            return True

    def vertical(self, step_to: ChessPoint):
        """verifies if figure is going vertical"""
        if self.__current_point__.x == step_to.x:
            return True

    def diagonal(self, step_to: ChessPoint):
        """verifies if figure is going diagonally"""
        if math.fabs(self.__current_point__.x - step_to.x) == math.fabs(self.__current_point__.y - step_to.y):
            return True

    def step(self, step_to: ChessPoint):
        """method moves the figure to the specific point, given by argument step_to: ChessPoint
        Also validates if move will not violate rules for the specific figure (each figure class must implement
        method valid, which will define the rules)"""
        if not inboard(step_to):
            raise OutOfBoard
        if step_to.x == self.__current_point__.x and step_to.y == self.__current_point__.y:
            raise NoMove
        if not self.valid(step_to):
            raise InvalidMove
        self.__current_point__.x = step_to.x
        self.__current_point__.y = step_to.y
        return True

    def __str__(self):
        return "{} object on {}{}".format(self.__color__, self.__current_point__.x, self.__current_point__.y)


class King(Figure):
    """Class defines figure King"""
    def valid(self, step_to: ChessPoint):
        """method defines move rules for king"""
        if math.fabs(ord(step_to.x) - ord(self.__current_point__.x)) > 1 or math.fabs(step_to.y - self.__current_point__.y) > 1:
            raise InvalidMove
        return True


class Queen(Figure):
    """Class defines figure Queen"""
    def valid(self, step_to: ChessPoint):
        """method defines move rules for queen"""
        if not (self.vertical(step_to) or self.horizontal(step_to) or self.diagonal(step_to)):
            raise InvalidMove
        return True


class Bishop(Figure):
    """Class defines figure Bishop"""
    def valid(self, step_to: ChessPoint):
        """method defines move rules for bishop"""
        if not self.diagonal(step_to):
            raise InvalidMove
        return True


class Knight(Figure):
    """Class defines figure Knight"""
    def valid(self, step_to: ChessPoint):
        """method defines move rules for knight"""
        if not ((math.fabs(ord(self.__current_point__.x) - ord(step_to.x)) == 2 and
                 math.fabs(self.__current_point__.y - step_to.y) == 1) or
                (math.fabs(ord(self.__current_point__.x) - ord(step_to.x)) == 1 and
                 math.fabs(self.__current_point__.y - step_to.y) == 2)):
            raise InvalidMove
        return True


class Rook(Figure):
    """Class defines figure Rook"""
    def valid(self, step_to: ChessPoint):
        """method defines move rules for rook"""
        if not (self.vertical(step_to) or self.horizontal(step_to)):
            raise InvalidMove
        return True


class Pawn(Figure):
    """Class defines figure Pawn"""
    def valid(self, step_to: ChessPoint):
        """method defines move rules for pawn"""
        if (self.__color__ == COLOR_WHITE) and (self.__current_point__.y == Y[1]):
            if not (step_to.y == Y[2] and math.fabs(ord(step_to.x) - ord(self.__current_point__.x)) <= 1):
                raise InvalidMove
            if not (step_to.y == Y[3] and step_to.x == self.__current_point__.x):
                raise InvalidMove
            if not (step_to.y - self.__current_point__.y == 1 and math.fabs(step_to.x - self.__current_point__.x) <= 1):
                raise InvalidMove
        if (self.__color__ == COLOR_BLACK) and (self.__current_point__.y == Y[-2]):
            if not (step_to.y == Y[-3] and math.fabs(ord(step_to.x) - ord(self.__current_point__.x)) <= 1):
                raise InvalidMove
            if not (step_to.y == Y[-4] and step_to.x == self.__current_point__.x):
                raise InvalidMove
            if not (self.__current_point__.y - step_to.y == 1 and math.fabs(ord(step_to.x) - ord(self.__current_point__.x)) <= 1):
                raise InvalidMove
        return True


if __name__ == '__main__':
    point = ChessPoint('A', 1)
    point_to = ChessPoint('B', 3)
    king = King(COLOR_WHITE, point)
    print("King {}".format(king))
    try:
        king.step(point_to)
    except OutOfBoard:
        print("King cannot go to out of board ({})".format(point))
    except NoMove:
        print("King cannot go to the place it stands on {}".format(point_to))
    except InvalidMove:
        print("King cannot go to {}, as it violates rules".format(point_to))

    print("King {}".format(king))
    # figures_types = (King, Queen, Bishop, Knight, Rook, Pawn)
    # moves= {1:"x+",
    #         2:"x+y+",
    #         3:"y+",
    #         4:"x-y+",
    #         5:"x-",
    #         6:"x-y-",
    #         7:"y-",
    #         8:"x+y-"}
    #
    # for steps in range(1,4):
    #     for move in moves.keys():
    #         for figure_type in figures_types:
    #             init_point = ChessPoint(random.choice(list(X)), random.choice(list(Y)))
    #             figure = figure_type(random.choice(list(COLOR)), init_point)
    #             try:
    #                 move_figure(figure, moves[move], steps)
    #             except OutOfBoard:
    #                 print("King cannot go to out of board ({})".format(point))
    #             except NoMove:
    #                 print("King cannot go to the place it stands on {}".format(point_to))
    #             except InvalidMove:
    #                 print("King cannot go to {}, as it violates rules".format(point_to))