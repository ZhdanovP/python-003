import itertools
from pieces import *
"""Chess game
__________________________________
8| R | N | B | K | Q | B | N | R | 
7| P | P | P | P | P | P | P | P |    < - black side 
6|   |   |   |   |   |   |   |   | 
5|   |   |   |   |   |   |   |   | 
4|   |   |   |   |   |   |   |   | 
3|   |   |   |   |   |   |   |   | 
2| p | p | p | p | p | p | p | p |    < -white side  
1| r | n | b | q | k | b | n | r | 
 --------------------------------   
 | a | b | c | d | e | f | g | h |
player play for both sides. 
White starts 
"""
class Game:
    """
    Board build, business logic, user input processing, run processing, 
    """
    def __init__(self):
        self.playersturn = WHITE
        self.gameboard = {}
        self.placeFigures()
        self.message="make your turn: e.g. \"a2 a3\" :"
        self.main()

    def placeFigures(self):
        for i in range(0,8):
            self.gameboard[(i,1)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
            self.gameboard[(i,6)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)            
        placers = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]        
        for i in range(0,8):
            self.gameboard[(i,0)] = placers[i](WHITE,uniDict[WHITE][placers[i]])
            self.gameboard[((7-i),7)] = placers[i](BLACK,uniDict[BLACK][placers[i]])
        placers.reverse()

    
    def main(self):
        
        while True:
            self.printBoard()
            print(self.message, end="")
            self.message = "> "
            startpos,endpos = self.parseInput()
            try:
                target = self.gameboard[startpos]
            except:
                self.message = "could not find piece; index out of range:"
                target = None
                
            if target:
                print("found "+str(target))
                if target.Color != self.playersturn:
                    self.message = "you aren't allowed to move that piece this turn"
                    continue
                if target.isValid(startpos,endpos,target.Color,self.gameboard):
                    self.message = "that is a valid move:"
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]
                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else : self.playersturn = BLACK
                else : 
                    self.message = "invalid move" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                    print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
            else : self.message = "there is no piece in that space, please repeat :"
    def printBoard(self):
        print("_"*33); 
        for i in range(0,8):
            print(8-i,end="| ")
            for j in range(0,8):
                item = self.gameboard.get((j,7-i)," ")
                print(str(item)+' |', end = " ")
            print()
        print("-"*34)
        print(" | a | b | c | d | e | f | g | h |")

    def parseInput(self):
        try:
            a,b = input().split()
            a = ((ord(a[0])-97), int(a[1])-1)
            b = (ord(b[0])-97, int(b[1])-1)
            print(a,b)
            return (a,b)
        except:
            print("error decoding input. please try again")
            return((-1,-1),(-1,-1))

#Game()