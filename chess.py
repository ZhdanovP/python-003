import random
""" Class Board simulates chess board with 8 random figures"""


class Board:
    """ Generating vhess board with
        random 8 figures"""
    d = [0] * 8
    for i in range(8):
        d[i] = [0] * 8
    for i in range(8):
        d[i][random.randint(0, 7)] = 1


""" Class Pawn simulates pawn on chess board"""


class Pawn:
    """ Setting pawn position
    using coordinates from 0 to 7
    starting from bottom left corner
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    """ Checking possible moves of Pawn on the field -> bolean"""
    def step(self, x1, y1):
        step_possible = False

        if (y1 - self.y) == 1 and (self.x - x1) == 0:
            step_possible = True

        if abs(self.x - x1) == 0 and abs(self.y - y1) == 0:
            step_possible = False
        elif x1 > 7 or x1 < 0:
            step_possible = False
        elif y1 > 7 or y1 < 0:
            step_possible = False
        elif Board.d[y1][x1] == 1:
            step_possible = False
        return step_possible


""" Class King simulates king on chess board"""


class King:
    """ Setting king position
    using coordinates from 0 to 7
    starting from bottom left corner
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """ Checking possible moves of King on the field -> bolean"""
    def step(self, x1, y1):
        step_possible = False

        if abs(self.y - y1) == 1 and abs(self.x - x1) == 0:
            step_possible = True
        if abs(self.x - x1) == 1 and abs(self.y - y1) == 0:
            step_possible = True
        if abs(self.x - x1) == 1 and abs(self.y - y1) == 1:
            step_possible = True

        if abs(self.x - x1) == 0 and abs(self.y - y1) == 0:
            step_possible = False
        elif x1 > 7 or x1 < 0:
            step_possible = False
        elif y1 > 7 or y1 < 0:
            step_possible = False
        elif Board.d[y1][x1] == 1:
            step_possible = False
        return step_possible


""" Class Qeen simulates Qeen on chess board"""


class Qeen:
    """ Setting Qeen position
    using coordinates from 0 to 7
    starting from bottom left corner
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """ Checking possible moves of Qeen on the field -> bolean"""
    def step(self, x1, y1):
        step_possible = False

        if abs(self.y - y1) >= 1 and abs(self.x - x1) == 0:
            step_possible = True
        if abs(self.x - x1) >= 1 and abs(self.y - y1) == 0:
            step_possible = True
        if abs(self.x - x1) == abs(self.y - y1):
            step_possible = True

        if abs(self.x - x1) == 0 and abs(self.y - y1) == 0:
            step_possible = False
        elif x1 > 7 or x1 < 0:
            step_possible = False
        elif y1 > 7 or y1 < 0:
            step_possible = False
        elif Board.d[y1][x1] == 1:
            step_possible = False
        return step_possible


# Some tests
print("Test 0")
i = 7
while i > -1:
    print(Board.d[i])
    i -= 1

print("Test 1")
p1 = Pawn(3, 3)
print(p1.step(3, 4))
print(p1.step(3, 3))
print(p1.step(3, 2))
print(p1.step(2, 3))
print(p1.step(4, 3))
print(p1.step(2, 2))
print(p1.step(4, 5))
print(p1.step(4, 8))
print(p1.step(-1, 2))
print("Test 2")
k1 = King(3, 3)
print(k1.step(3, 2))
print(k1.step(3, 4))
print(k1.step(4, 3))
print(k1.step(2, 3))
print(k1.step(4, 4))
print(k1.step(2, 2))
print(k1.step(4, 5))
print(k1.step(4, 8))
print(k1.step(-1, 2))
print("Test 3")
q1 = Qeen(3, 3)
print(q1.step(0, 0))
print(q1.step(7, 7))
print(q1.step(0, 3))
print(q1.step(3, 0))
print(q1.step(8, 3))
print(q1.step(4, 7))
