from mytests.decor import my_decorator
import time

@my_decorator
def test_board(b1):
    print("Test Board")
    i = 7
    while i > -1:
        print(b1.d[i])
        time.sleep(1)
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
    time.sleep(2)

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
    time.sleep(2)

@my_decorator
def test_qeen(q1, b1):
    print("Test Qeen")
    print(q1.step(0, 0, b1))
    print(q1.step(7, 7, b1))
    print(q1.step(0, 3, b1))
    print(q1.step(3, 0, b1))
    print(q1.step(8, 3, b1))
    print(q1.step(4, 7, b1))
    time.sleep(2)
