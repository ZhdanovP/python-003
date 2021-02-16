"""
Chess game
not oop solution

"""
gameboard={}
color_ =   ["black", "white"]
figures_ = ["Rook ","Knight","Bishop","Queen","King ","Bishop","Knight","Rook "]

def build_board():
    for i in range(8): gameboard[(0,i)] = (color_[0],figures_[i])
    for i in range(8): gameboard[(1,i)] = (color_[0],"Pawn ") 
    for i in range(2,6): 
        for j in range(0,8): gameboard[(i,j)] = ("     ","empty")  
    for i in range(8): gameboard[(6,i)] = (color_[1],"Pawn")
    for i in range(8):  gameboard[(7,(7-i))] = (color_[1],figures_[i])      
    pass

def print_board():
    for i in range (8):
        for j in range (8):
            print(gameboard[i,j],end =" " ) 
        print()            

def whats_here(x1_, y1_):
    ret_=gameboard[x1_,y1_]
    return ret_

def isMoveAllowed(x2,y2,whats_here_):
    whats_here1_=whats_here(x2,y2)
    if (whats_here1_[1]=="empty"):
        print("run is allowed here")
        return True
    else:
        print(f"this cell is occupied by {whats_here1_}")
        return False


def allowed_moves(whats_here,x_,y_):
    allowed_moves={}    
    if (whats_here=="Pawn"):
        print(f"Case {whats_here}")
        allowed_moves={x_,y+1}
    elif(whats_here=="Rock"):
        print(f"Case {whats_here}") #build all variants dict max <=14)
        allowed_moves={(x_,0),(x_,1),(x_,2),(x_,3),(x_,4),(x_,5),(x_,6),(x_,7),
        (0,y_),(1,y_),(2,y_),(3,y_),(4,y_),(5,y_),(6,y_),(7,y_)}            
    elif(whats_here=="Knight"):
        print(f"Case {whats_here}") #build all variants dict max <=8)
        allowed_moves_={(x_+2,y_+1),(x_+1,y+2),(x_-1,y+2),(x_-2,y+1),(x_-2,y-1),(x_-1,y-2),(x_+1,y-1),(x_+2,y-1)}
    elif(whats_here=="Bishop"):
        print(f"Case {whats_here}") #build all variants dict, max <= 14
        allowed_moves_={(x_-7,y_-7),(x_-6,y-6),(x_-5,y-5),(x_-4,y-4),(x_-3,y-3),(x_-2,y-2),(x_-1,y-1),
        (x_+7,y_+7),(x_+6,y+6),(x_+5,y+5),(x_+4,y+4),(x_+3,y+3),(x_+2,y+2),(x_+1,y+1)    }
    elif(whats_here=="Queen"):
        print(f"Case {whats_here}")  #1 build all variants dict max <=27
        allowed_moves_={(x_-7,y_-7), (x_-6,y-6), (x_-5,y-5), (x_-4,y-4), (x_-3,y-3), (x_-2,y-2), (x_-1,y-1),
        (x_+7,y_+7), (x_+6,y+6), (x_+5,y+5), (x_+4,y+4), (x_+3,y+3), (x_+2,y+2), (x_+1,y+1),
        (x_,0), (x_,1), (x_,2), (x_,3), (x_,4), (x_,5), (x_,6), (x_,7),
        (0,y_), (1,y_), (2,y_), (3,y_), (4,y_), (5,y_), (6,y_), (7,y_) }
    elif (whats_here=="King"):
        print(f"Case {whats_here}")    #1 build all variants dict max <=8
        allowed_moves_={(x_+1,y_), (x_-1,y), (x_,y+1), (x_,y-1), (x_+1,y+1), (x_-1,y-1), (x_+1,y-1), (x_-1,y+1)}
    #2 remove variants of dairs from dict where x_ or y_<0, or x or y>7 -  todo
    
    return allowed_moves

def check_move(x1_,y1_,x2_,y2_):
    whats_here_=whats_here(x1_,y1_)
    allowed_moves_=allowed_moves(x1_,y1_,whats_here_[1])
    if(isMoveAllowed(x2_,y2_,whats_here_)):
        gameboard[x2_,y2_]=gameboard[x1_,y1_]
        gameboard[x1_,y1_]=("     ","empty") 
        print_board()   
    pass


def main():
    build_board()
    print_board()
    try:
        while True:
            y1,x1,y2,x2=input("enter your run:x1 y1 x2 y2:").split(" ") 
            print ("x1 = "+x1+", y1 = "+y1+", x2 = "+x2+", y2 = "+y2)
            x1,y1,x2,y2 = [int(x) for x in [x1, y1, x2, y2]]
            x1=8-x1;y1=y1-1;x2=8-x2;y2=y2-1
            print(whats_here(x1,y1));  print(whats_here(x2,y2)); 
            check_move(x1,y1,x2,y2)
    except KeyboardInterrupt:
        pass

main()