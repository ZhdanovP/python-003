from pieces_.pieces import Piece as Piece
from pieces_.pieces import chessDiagonals as chessDiagonals, chessCardinals as chessCardinals
from pieces_.AdNauseum import AdNauseum

class Queen(Piece,AdNauseum):
    """ Queen piece - move in all direction
    """
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals+chessDiagonals)
    
