from symbol import decorator

from myfigures.figures import Pawn, King, Qeen
from mytests import tests
import random

"""Module simulates chess board with 8 random figures
 and their movement"""


class Board:
    """ Generating chess board with
        random 8 figures"""
    d = list()

    def empty(self):
        self.d = [0] * 8
        for i in range(8):
            self.d[i] = [0] * 8
        for i in range(8):
            self.d[i][i] = 0

    def rand(self):
        for i in range(8):
            self.d[i][random.randint(0, 7)] = 1


# Execute Some tests
b1 = Board()
b1.empty()
b1.rand()
tests.test_board(b1)

p1 = Pawn(3, 3)
tests.test_pawn(p1, b1)

k1 = King(3, 3)
tests.test_king(k1, b1)

q1 = Qeen(3, 3)
tests.test_qeen(q1, b1)


