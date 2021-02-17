from myfigures.figures import Pawn, King, Qeen, Board
from mytests import tests

"""Module simulates chess board with 8 random figures
 and their movement"""

# Execute Some tests
b1 = Board()
tests.test_0(b1)

p1 = Pawn(3, 3)
tests.test_1(p1)

k1 = King(3, 3)
tests.test_2(k1)

q1 = Qeen(3, 3)
tests.test_3(q1)


