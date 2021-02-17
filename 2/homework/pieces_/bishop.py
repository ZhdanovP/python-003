from pieces_.pieces import Piece as Piece
from pieces_.pieces import chessDiagonals as chessDiagonals
from pieces_.AdNauseum import AdNauseum as AdNauseum

class Bishop(Piece,AdNauseum):
    """Bishop move in dioganals on one only colors, an inherited AdNuseum behaviour
    """
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessDiagonals)