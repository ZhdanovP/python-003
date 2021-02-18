def my_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format((end - start)))
        return return_value
    return wrapper

@my_decorator
def test_board(b1):
    print("Test Board")
    i = 7
    while i > -1:
        print(b1.d[i])
        i -= 1

@my_decorator
def test_pawn(p1, b1):
    print("Test Pawn")
    print(p1.step(3, 4, b1))
    print(p1.step(3, 3, b1))
    print(p1.step(3, 2, b1))
    print(p1.step(2, 3, b1))
    print(p1.step(4, 3, b1))
    print(p1.step(2, 2, b1))
    print(p1.step(4, 5, b1))
    print(p1.step(4, 8, b1))
    print(p1.step(-1, 2, b1))

@my_decorator
def test_king(k1, b1):
    print("Test King")
    print(k1.step(3, 2, b1))
    print(k1.step(3, 4, b1))
    print(k1.step(4,3, b1))
    print(k1.step(2, 3, b1))
    print(k1.step(4, 4, b1))
    print(k1.step(2, 2, b1))
    print(k1.step(4, 5, b1))
    print(k1.step(4, 8, b1))
    print(k1.step(-1, 2, b1))

@my_decorator
def test_qeen(q1, b1):
    print("Test Qeen")
    print(q1.step(0, 0, b1))
    print(q1.step(7, 7, b1))
    print(q1.step(0, 3, b1))
    print(q1.step(3, 0, b1))
    print(q1.step(8, 3, b1))
    print(q1.step(4, 7, b1))
