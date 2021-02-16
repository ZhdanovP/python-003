from figures import Pawn, King, Qeen, Board
from tests import *

"""Module simulates chess board with 8 random figures
 and their movement"""

# Execute Some tests
b1 = Board()
test_0(b1)

p1 = Pawn(3, 3)
test_1(p1)

k1 = King(3, 3)
test_2(k1)

q1 = Qeen(3, 3)
test_3(q1)


