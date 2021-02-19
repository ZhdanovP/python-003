class Matrix:
    """ Generating 2x2 matrix"""
    d = list()

    def empty(self):
        """Cretes Empty board 8x8"""
        self.d = [0] * 2
        for i in range(2):
            self.d[i] = [0] * 2
        for i in range(2):
            self.d[i][i] = 0

    def print(self):
        for i in range(2):
            print(self.d[i])

    def __add__(self, other):
        for i in range(2):
            for j in range(2):
                self.d[i][j] = self.d[i][j] + other.d[i][j]
        return self

    def __mul__(self, other):
        for i in range(2):
            for j in range(2):
                self.d[i][j] = self.d[i][j] * other
        return self

m1 = Matrix()
m1.empty()
m1.d[0][0] = 1
m1.d[1][1] = 1
m1.print()

m2 = Matrix()
m2.empty()
m2.d[0][0] = 2
m2.d[1][1] = 2
m2.print()

m3 = m1 + m2
m1.print()
m2.print()
m3.print()

m4 = m2 * 4
m2.print()
m4.print()
