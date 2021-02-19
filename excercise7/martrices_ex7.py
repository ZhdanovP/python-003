import operator


class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.lst)

    def __add__(self, num):
        res_mtrx = Matrix([])
        for row in self.lst:
            res_mtrx.lst.append([col + num for col in row])
        return res_mtrx

    __radd__ = __add__

    def __mul__(self, num):
        def mul(row, col):
            return sum(a * b for a, b in zip(row, col))

        res_mtrx = Matrix([])
        for row in self.lst:
            if isinstance(num, int):
                res_mtrx.lst.append([col * num for col in row])
            else:
                res_mtrx.lst.append([mul(row, col) for col in zip(*num.lst)])
        return res_mtrx

    __rmul__ = __mul__

    def __bool__(self):
        res = []
        for row in self.lst:
            for r in row:
                if r == 0:
                    res.append(r)
        return len(res) == 0


mtx = [
        [2, 2, 3],
        [10, 20, 25],
        [11, 50, 5]
    ]

m = Matrix(mtx)
print(m * 10)
print('__________')
print(m + 5)
print(m.__bool__())
print('__________')
print(20 * m)
print('__________')
print(2 + m)