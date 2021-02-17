import string
"""
Chess game.
Functional (not OOP) solution.
Functionality: board filled with black and white chess 
User enter run coordinate if Format From - To  1 2 1 3  mean a2 a3
if run is allowed figure moved to allowed position and board re-buided
"""

gameboard={}
color_ =   ["black","white"]
figures_ = ["Rook_","Knigh","Bisho","Queen","King_","Bisho","Knigh","Rook_"]

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive. subsidary def for char based coordinartess
    """
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def build_board():
    for i in char_range('a','h'):
        for j in range(1,9): gameboard[(i,j)] = ("     ","     ")    
    
    #for ch in char_range('a','h'):print(gameboard[(ch,1)]);  gameboard[(ch,1)] = (color_[0],figures_[ord(ch)-96]);  print(gameboard[(ch,1)])

    for ch in char_range('a','h'): gameboard[(ch,1)] = (color_[0],figures_[ord(ch)-97])
    for ch in char_range('a','h'): gameboard[(ch,2)] = (color_[0],"Pawn_")
    for ch in char_range('a','h'): gameboard[(ch,7)] = (color_[1],"Pawn_")
    for ch in char_range('a','h'): gameboard[(ch,8)] = (color_[1],figures_[ord(ch)-97])
    #for i in range('a','h'): gameboard[(0,i)] = (color_[0],figures_[i])
    #for i in range(8): gameboard[(1,i)] = (color_[0],"Pawn_") 
    #for i in range(2,6): for j in range(0,8): gameboard[(i,j)] = ("     ","Empty")  
    #for i in range(8): gameboard[(6,i)] = (color_[1],"Pawn_")
    #for i in range(8):  gameboard[(7,(7-i))] = (color_[1],figures_[i])      
    #pass

def print_board():
    print("    ---------a---------------b-----------------c-------------------d------------------e------------------f-----------------g------------------h-------   ")
    for j in range (1,9):
        print(f"{9-j}",end =" ")
        for i in char_range ('a','h'):
            print(gameboard[i,9-j],end =" " )
        print();#print(f"------------------------------------------------------------------------------------------------------------------------------------------------")
#build_board();print_board()     

def whats_here(ch_, int_):
    ret_=gameboard[(ch_,int_)]
    return ret_

def isMoveAllowed_to(x1,y1,whats_here_):
    if (whats_here_[1]=="     "):
        print(f"move allowed")
        return True
    elif((whats_here(x1,y1)[0])!=whats_here_[0]):
        if((whats_here(x1,y1)[0])!="Pawn_"):
            print("we hit enemy!")
            return True
    else:
        print(f"this cell is occupied by {whats_here_}")
        return False

def allowed_moves(x_,y_,cell_occupied_by,to_):
    allowed_moves={};allowed_moves_={}    
    if (cell_occupied_by=="Pawn_"):
        print(f"Case {cell_occupied_by}")
        if(to_[1]!="    "):
            allowed_moves={(x_,y_+1),(chr(ord(x_)+1),y_+1),(chr(ord(x_)-1),y_+1)}   #if hit for Pawn_ is allowed  
        else:
            allowed_moves={(x_,y_+1)}
    elif(cell_occupied_by=="Rook_"):
        print(f"Case {cell_occupied_by}") #build all variants dict max <=14)
        allowed_moves={(x_,0),(x_,1),(x_,2),(x_,3),(x_,4),(x_,5),(x_,6),(x_,7),
        ('a',y_),('b',y_),('c',y_),('d',y_),('e',y_),('f',y_),('g',y_),('h',y_)}            
    elif(cell_occupied_by=="Knigh"):
        print(f"Case {cell_occupied_by}") #build all variants dict max <=8)
        allowed_moves={(chr(ord(x_)+2),y_+1),(chr(ord(x_)+1),y_+2),(chr(ord(x_)-1),y_+2),(chr(ord(x_)-2),y_+1),(chr(ord(x_)-2),y_-1),(chr(ord(x_)-1),y_-2),(chr(ord(x_)+1),y_-1),(chr(ord(x_)+2),y_-1)}
    elif(cell_occupied_by=="Bisho"):
        print(f"Case {cell_occupied_by}") #build all variants dict, max <= 14
        allowed_moves={(chr(ord(x_)-7),y_-7),(chr(ord(x_)-6),y_-6),(chr(ord(x_)-5),y_-5),(chr(ord(x_)-4),y_-4),(chr(ord(x_)-3),y_-3),(chr(ord(x_)-2),y_-2),(chr(ord(x_)-1),y_-1),
        (chr(ord(x_)+7),y_+7),(chr(ord(x_)+6),y+6),(chr(ord(x_)+5),y_+5),(chr(ord(x_)+4),y_+4),(chr(ord(x_)+3),y_+3),(chr(ord(x_)+2),y_+2),(chr(ord(x_)+1),y_+1)    }
    elif(cell_occupied_by=="Queen"):
        print(f"Case {cell_occupied_by}")  #1 build all variants dict max <=27
        allowed_moves={(chr(ord(x_)-7),y_-7), (chr(ord(x_)-6),y_-6), (chr(ord(x_)-5),y_-5), (chr(ord(x_)-4),y_-4), (chr(ord(x_)-3),y_-3), (chr(ord(x_)-2),y_-2), (chr(ord(x_)-1),y_-1),
        (chr(ord(x_)+7),y_+7), (chr(ord(x_)+6),y_+6), (chr(ord(x_)+5),y_+5), (chr(ord(x_)+4),y_+4), (chr(ord(x_)+3),y_+3), (chr(ord(x_)+2),y_+2), (chr(ord(x_)+1),y_+1),
        (x_,0), (x_,1), (x_,2), (x_,3), (x_,4), (x_,5), (x_,6), (x_,7),
        ('a',y_), ('b',y_), ('c',y_),('d',y_),('e',y_),('f',y_), ('g',y_), ('h',y_) }
    elif (cell_occupied_by=="King_"):
        print(f"Case {cell_occupied_by}")    #1 build all variants dict max <=8
        allowed_moves={(chr(ord(x_)+1),y_), (chr(ord(x_)-1),y_), (x_,y_+1), (x_,y_-1), (chr(ord(x_)+1),y_+1), (chr(ord(x_)-1),y_-1), (chr(ord(x_)+1),y_-1), (chr(ord(x_)-1),y_+1)}
    elif (cell_occupied_by=="     "):
        print(f"Case {cell_occupied_by}") 
        print("Not possible to run, start point is empty")
        allowed_moves={}


    # check if each of pairs inside allowed_moves_ are in range 'a':'h', 1-8, if not remove such a pair
    allowed_moves_=set(allowed_moves);print(allowed_moves)  
    for elem in allowed_moves:
        if ( (ord(elem[0])<97) or (ord(elem[0])>104)  ):
            print(f"{elem} shall be removed")
            allowed_moves_.remove(elem)
        elif( (elem[1])<1 or (elem[1])>8 ):
            print(f"{elem} shall be removed")
            allowed_moves_.remove(elem)
        
    print(allowed_moves_) 
    return allowed_moves_


def isToInAllowed(ch2_,int2_,allowed):
    for elem in allowed:
        if(elem[0]==ch2_):
            if (elem[1]==int2_):
                print("desired move in allowed")
                return True
        
    return False

def move(ch1_,int1_,ch2_,int2_):
    from_=whats_here(ch1_,int1_)
    to_=whats_here(ch2_,int2_)

    allowed_moves_from=allowed_moves(ch1_,int1_,from_[1],to_)
    if(isToInAllowed(ch2_,int2_,allowed_moves_from)):
        print("we can move")
        gameboard[ch2_,int2_]=gameboard[ch1_,int1_]
        gameboard[ch1_,int1_]=("     ","     ") 
        print_board()
        return True
    else:
        print(f"we can move to {ch2_,int2_}")
        print_board()
        return False
    pass

def main():
    build_board()
    print_board()
    try:
        while True:
            ch1, int1, ch2, int2=input("enter your run:x1 FromCharIntToCharInt e.g.a 2 a 3 mans move a2 -> a3:").split() 
            int1,int2 = [int(x) for x in [int1, int2]]
            move(ch1,int1,ch2,int2)
    except KeyboardInterrupt:
        pass
main()