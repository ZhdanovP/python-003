from abc import ABC
class AdNauseum(ABC):
    """This is a behaviour we inherited for Qneen, Bishop and Rook
    """
    @classmethod
    def AdNauseum(self, x, y, gameboard, Color, intervals):
        """
        for long distance runniing figures Qneen, Bishop,Rook, if enemy on the pssible way we add option to hit it to possible run(s)        
        repeats the given interval until another piece is run into. if that piece is not of the same color, that square is added and then the list is returned        
        """
        answers = []
        for xint, yint in intervals:
            xtemp, ytemp = x + xint, y + yint
            while (xtemp >= 0 and xtemp < 8 and ytemp >= 0 and ytemp < 8):
            #while self.isInBounds(xtemp, ytemp):
                target = gameboard.get((xtemp, ytemp), None)
                if target is None:
                    answers.append((xtemp, ytemp))
                elif target.Color != Color:
                    answers.append((xtemp, ytemp))
                    break
                else:
                    break
                xtemp, ytemp = xtemp + xint, ytemp + yint
        return answers