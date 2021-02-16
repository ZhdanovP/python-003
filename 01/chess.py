"""1 king  2 queen. 2 rooks.  2 bishops - officer.   2 knights - kon'. 8 pawns. 
# Design a chess piece class. 
# For each type of figure, make a separate class. 
# Implement the step() method, which will check if the move specified by the user is possible. The figures on the field
# are arranged randomly. The figure cannot go to any field in which it is already standing. 
"""
whose_run=1 # 1- run on white, 0 run on black side;
color_ =   ["black", "white"]
figures_ = ["Rook","Knight","Bishop","Queen","King","Bishop","Knight","Rook"]
moves =[] ; # short notation P=["P","P","P","P","P","P","P","P"]; Fs=["R","K","B","Q","Ki","B","K","R"]


class Game:
    def __init__(self):
        self.gameboard = {}
        self.message="Make a run (ex.:a2 a3)"
        self.placePieces()
        self.main()
        

    def placePieces(self):
        """ this method stand for locate pices on board
        """
        for i in range(0,8):
            self.gameboard[(i,1)] = (color_[0],"Pawn")
            self.gameboard[(i,6)] = (color_[1],"Pawn")
        
        for i in range(0,8):
            self.gameboard[(i,0)] = (color_[0],figures_[i])
            self.gameboard[((7-i),7)] = (color_[1],figures_[i])

    def what_figure_incel(self):
        pass

    def move(self):
        pass
    
    def main(self):
            while True:
                print(self.message)
                self.message = ""
                startpos,endpos = self.parseInput()
                try:
                    target = self.gameboard[startpos]
                except:
                    self.message = "could not find piece; index probably out of range"
                    target = None
                    
                if target:
                    print("found "+str(target))
                    if target.Color != self.playersturn:
                        self.message = "you aren't allowed to move that piece this turn"
                        continue
                    if target.isValid(startpos,endpos,target.Color,self.gameboard):
                        self.message = "that is a valid move"
                        self.gameboard[endpos] = self.gameboard[startpos]
                        del self.gameboard[startpos]
                        self.isCheck()
                        if self.playersturn == BLACK:
                            self.playersturn = WHITE
                        else : self.playersturn = BLACK
                    else : 
                        self.message = "invalid move" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                        print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                else : self.message = "there is no piece in that space"


class Piece:
    def __init__(self,color,name):
        self.name = name
        self.position = None
        self.Color = color
    def isValid(self,startpos,endpos,Color,gameboard):
        if endpos in self.availableMoves(startpos[0],startpos[1],gameboard, Color = Color):
            return True
        return False

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name

    def availableMoves(self,x,y,gameboard):
        print("ERROR: no movement for base class")
    
    def AdNauseum(self,x,y,gameboard, Color, intervals):
        """repeats the given interval until another piece is run into. 
        if that piece is not of the same color, that square is added and
         then the list is returned"""
        answers = []
        for xint,yint in intervals:
            xtemp,ytemp = x+xint,y+yint
            while self.isInBounds(xtemp,ytemp):
                target = gameboard.get((xtemp,ytemp),None)
                if target is None: answers.append((xtemp,ytemp))
                elif target.Color != Color: 
                    answers.append((xtemp,ytemp))
                    break
                else:
                    break
                
                xtemp,ytemp = xtemp + xint,ytemp + yint
        return answers
    
    def isInBounds(self,x,y):
        "checks if a position is on the board"
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False
    
    def noConflict(self,gameboard,initialColor,x,y):
        "checks if a single position poses no conflict to the rules of chess"
        if self.isInBounds(x,y) and (((x,y) not in gameboard) or gameboard[(x,y)].Color != initialColor) : return True
        return False


Game()



"""TODO -5. implement base figures class
TODO -4. implement base figures methods /         - inside figures classes implement is_allowed method
TODO -3. implement base game class
TODO -2. implement base game method

TODO 1. Classes realization
TODO 2. Classes interaction 
TODO 3. Method MOVE for each Figure
TODO 4. Exceprion processing 
(opt TODO 5 : Chekc if Place is already occupied by other pices  
(opt TODO 6:place on field 16 black and 16 whaite figures
(opr TODO 7:todocreate_board)
? where shall i store board;
board contains link to objet

Assumprion(s): - no BL is implemented
- no foes logyc implemented
- no checkmate logyc lmplemented
- no enemy move uimplemented
- not kill posssible, just move forbidden
- board marked as a1 lowest left h8 hightst top
- moves looks like: a2 a4
class pawn(Piece):
    def __init__(self, color,name,direction):
        self.name = name
        self.Color = color
        self.direction = direction
        pass
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        answers = []
        if (x+1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x+1, y+self.direction) : answers.append((x+1,y+self.direction))
        if (x-1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x-1, y+self.direction) : answers.append((x-1,y+self.direction))
        if (x,y+self.direction) not in gameboard and Color == self.Color : answers.append((x,y+self.direction))# the condition after the and is to make sure the non-capturing movement (the only fucking one in the game) is not used in the calculation of checkmate
        return answers


class Figure:
    def __init__(self, fig_name, bw_, pos_x,pos_y):
        self.fig_name = fig_name
        self.bw_=bw_
        self.pos_x=pos_x
        self.pos_y=pos_y
        print("figure initialized")
    
    def checkIfmoveisAlloowed(self,fig_name,pox_x,pos_y,pos_x1,pos_y1):
        if(fig_name == 'queen'):
            print("queen run check")
            pass
        if(fig_name == 'king'):
            print("king  run check")
            pass
        if(fig_name == 'rock'):
            print("rock  run check")
            pass
        if(fig_name == 'bishop'):
            print("bishop run check")
            pass
        if(fig_name == 'knights'):
            print("knights run check")
            pass
        if(fig_name == 'pawns'):
            print("pawns run check")
            pass
            
    def move(self, fig_name, pos_x1,pos_y1):
        self.checkIfmoveisAlloowed(fig_name,pos_x,pos_y,pos_x1,pos_y1)        
        print("figure move")
        pass
      
class queen(Figure):
    def __init__(self,bw_,pos_x,pos_y):
        self.bw_=bw_
        self.pos_x=pos_x
        self.pos_y=pos_y
        super().__init__("queen", self.bw_, self.pos_x, self.pos_y)
    
    def show_(self):
        print(self.pos_x, self.pos_y,self.bw_)

    def move(self,pos_x1,pos_y1):
        print ("Queen move")
        self.move

q1=queen("white","a",1)
q1.show_()

"""