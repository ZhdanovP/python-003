from pieces_.pieces import Piece as Piece
from pieces_.pieces import chessDiagonals as chessDiagonals


class Knight(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return [(xx,yy) for xx,yy in knightList(x,y,2,1) if self.noConflict(gameboard, Color, xx, yy)]

def knightList(x, y, int1, int2):
    """sepcifically for the rook, permutes the values needed around a position for noConflict tests"""
    return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
            (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]