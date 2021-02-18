from abc import ABC, abstractmethod


class Figure(ABC):
    """ Absract interface"""
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def step(self, x1, y1):
        pass

class Pawn(Figure):
    """ Class Pawn simulates pawn on chess board"""
    __slots__ = ()

    def step(self, x1, y1, board):
        """ Checking possible moves of Pawn on the field -> bolean"""
        step_possible = False

        if (y1 - self.y) == 1 and (self.x - x1) == 0:
            step_possible = True

        if abs(self.x - x1) == 0 and abs(self.y - y1) == 0:
            step_possible = False
        elif x1 > 7 or x1 < 0:
            step_possible = False
        elif y1 > 7 or y1 < 0:
            step_possible = False
        elif board.d[y1][x1] == 1:
            step_possible = False
        return step_possible


class King(Figure):
    """ Class King simulates king on chess board"""
    __slots__ = ()

    def step(self, x1, y1, board):
        """ Checking possible moves of King on the field -> bolean"""
        step_possible = False

        if abs(self.y - y1) == 1 and abs(self.x - x1) == 0:
            step_possible = True
        if abs(self.x - x1) == 1 and abs(self.y - y1) == 0:
            step_possible = True
        if abs(self.x - x1) == 1 and abs(self.y - y1) == 1:
            step_possible = True

        if abs(self.x - x1) == 0 and abs(self.y - y1) == 0:
            step_possible = False
        elif x1 > 7 or x1 < 0:
            step_possible = False
        elif y1 > 7 or y1 < 0:
            step_possible = False
        elif board.d[y1][x1] == 1:
            step_possible = False
        return step_possible


class Qeen(Figure):
    """ Class Qeen simulates Qeen on chess board"""
    __slots__ = ()
    def step(self, x1, y1, board):
        """ Checking possible moves of Qeen on the field -> bolean"""
        step_possible = False

        if abs(self.y - y1) >= 1 and abs(self.x - x1) == 0:
            step_possible = True
        if abs(self.x - x1) >= 1 and abs(self.y - y1) == 0:
            step_possible = True
        if abs(self.x - x1) == abs(self.y - y1):
            step_possible = True

        if abs(self.x - x1) == 0 and abs(self.y - y1) == 0:
            step_possible = False
        elif x1 > 7 or x1 < 0:
            step_possible = False
        elif y1 > 7 or y1 < 0:
            step_possible = False
        elif board.d[y1][x1] == 1:
            step_possible = False
        return step_possible