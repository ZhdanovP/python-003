from abc import ABC, abstractmethod
import random
chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

class Piece(ABC):
    """ base class for piceces creation, 
    instancing forbiden
    is parrents for all pices on a board
    """
    __slots__ = ('name', 'position', 'Color')

    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.Color = color

    def isValid(self, startpos, endpos, Color, gameboard):
        if endpos in self.availableMoves(startpos[0], startpos[1], gameboard, Color=Color):
            return True
        return False
    #def __repr__(self):  #    return self.name
    def __str__(self):
        return self.name

    @abstractmethod
    def availableMoves(self, x, y, gameboard):
        pass
    
    def isInBounds(self, x, y):
        "checks if a position is on the board"
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def noConflict(self, gameboard, initialColor, x, y):
        "checks if a single position poses no conflict to the rules of chess"
        if self.isInBounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].Color != initialColor): return True
        return False