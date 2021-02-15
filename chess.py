class Pawn:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # using coordinates from 0 to 7
    # starting from bottom left corner

    def step(self, x1, y1):
        step_possible = True

        #no more then 1 step possible for pawn and only straight
        if abs(self.x-x1) != 0:
            step_possible = False

        elif abs(self.y-y1) > 1 or abs(self.y-y1) == 0:
            step_possible = False

        # check pawn can not move back
        elif (y1 - self.y) < 0:
            step_possible = False

        # check move not out of the desk
        elif x1 > 7 or x1 < 0:
            step_possible = False
        elif y1 > 7 or y1 < 0:
            step_possible = False

        return step_possible

p1 = Pawn(0,1)
print(p1.step(0, 2))
print(p1.step(0, 5))
