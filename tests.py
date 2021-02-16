def test_0(b1):
    print("Test Board")
    i = 7
    while i > -1:
        print(b1.d[i])
        i -= 1


def test_1(p1):
    print("Test Pawn")
    print(p1.step(3, 4))
    print(p1.step(3, 3))
    print(p1.step(3, 2))
    print(p1.step(2, 3))
    print(p1.step(4, 3))
    print(p1.step(2, 2))
    print(p1.step(4, 5))
    print(p1.step(4, 8))
    print(p1.step(-1, 2))


def test_2(k1):
    print("Test King")
    print(k1.step(3, 2))
    print(k1.step(3, 4))
    print(k1.step(4, 3))
    print(k1.step(2, 3))
    print(k1.step(4, 4))
    print(k1.step(2, 2))
    print(k1.step(4, 5))
    print(k1.step(4, 8))
    print(k1.step(-1, 2))


def test_3(q1):
    print("Test Qeen")
    print(q1.step(0, 0))
    print(q1.step(7, 7))
    print(q1.step(0, 3))
    print(q1.step(3, 0))
    print(q1.step(8, 3))
    print(q1.step(4, 7))
