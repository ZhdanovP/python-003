from copy import deepcopy


class Matrix:
    def __init__(self, matr):
        self._dimension = len(matr)
        self.matrix = deepcopy(matr)

    def __str__(self):
        ret = ''
        for i in range(self._dimension):
            for j in range(self._dimension):
                ret = ret + f'{self.matrix[i][j]:3} '
            ret = ret + '\n'
        return ret

    def __add__(self, other):
        ret = deepcopy(self.matrix)
        if isinstance(other, Matrix):
            for i in range(self._dimension):
                for j in range(self._dimension):
                    ret[i][j] = self.matrix[i][j] + other.matrix[i][j]
        else:
            for i in range(self._dimension):
                for j in range(self._dimension):
                    ret[i][j] = self.matrix[i][j] + other

        return Matrix(ret)

    def __mul__(self, scalar):
        ret = deepcopy(self.matrix)
        for i in range(self._dimension):
            for j in range(self._dimension):
                ret[i][j] = self.matrix[i][j] * scalar
        return Matrix(ret)

    def __bool__(self):
        for i in range(self._dimension):
            for j in range(self._dimension):
                if self.matrix[i][j] == 0:
                    return False
        return True


if __name__ == "__main__":
    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    m2 = [[11, 12, 13],
          [14, 15, 16],
          [17, 18, 19]]

    matr1 = Matrix(m1)
    matr2 = Matrix(m2)
    print(matr1)
    print(matr1 + matr2)
    print(matr1 + 1)
    print(matr1 * 10)
    if matr1:
        print('Non zero')
