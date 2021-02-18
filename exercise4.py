

class NoModulePredicate(object):
    __slots__ = 'divider'

    def __init__(self, divider):
        self.divider = divider

    def __call__(self, dividend):
        return 0 == (dividend % self.divider)


def sum_with_predicate(*args, predicate):
    total_sum = 0
    for num in args:
        if predicate(num):
            total_sum += num

    return total_sum


twoDiv = NoModulePredicate(2)
total_sum = sum_with_predicate(1, 2, 3, 4, 5, 6, predicate=twoDiv)
print(str(total_sum))
