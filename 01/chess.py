"""1 king      2 queen.   2 rooks - tura.  2 bishops - ofitser.   2 knights - kon'.     8 pawns. peshka"""
# Design a chess piece class. For each type of figure, make a separate class. 
#Implement the step() method, which will check if
#the move specified by the user is possible. The figures on the field
#are arranged randomly. The figure cannot go to any field in which it is already standing.

class Figure:
    """ figure class documentation"""
    def __init__(self, fig_name, bw_, pos_x,pos_y):
        self.fig_name = fig_name
        self.bw_=bw_
        self.pos_x=pos_x
        self.pos_y=pos_y
        print("figure initialized")
    
    def checkIfmoveisAlloowed(self,fig_name,pox_x,pos_y,pos_x1,pos_y1):
        """ if move is allowed method documentation"""

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
        @classmethod

       



q1=queen("white","a",1)
q1.show_()
q1.move()
