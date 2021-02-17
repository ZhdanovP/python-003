from pieces_.pieces import Piece as Piece
from pieces_.pieces import chessCardinals as chessCardinals
from pieces_.AdNauseum import AdNauseum as AdNauseum

class Rook(Piece,AdNauseum):
    """Rook pice move vertical and horizintal direction
    """
    def availableMoves(self,x,y,gameboard ,Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals)