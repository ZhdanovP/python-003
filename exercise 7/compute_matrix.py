class ComputeMatrix:
    def __init__(self, a: list, b: list):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + self.b

    def __radd__(self, other):
        return self.b + self.a

    def __mul__(self, other):
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in
                   zip(*self.b)] for X_row in self.a]
        return result

    def __rmul__(self, other):
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in
                   zip(*self.a)] for X_row in self.b]
        return result

    def __bool__(self):
        for i in self.a:
            if not i:
                return False
        for j in self.b:
            if not j:
                return False
        return True

    def __str__(self):
        return [self.a, self.b]

    def __repr__(self):
        return str([self.a, self.b])
