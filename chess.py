"""A simple chess piece algorithms."""
from knight import Knight
from pawn import Pawn


def setup_empty_board():
    """
    :return: A list of 8 lists each containing an 8 empty slots.
    """
    board = []
    for row in range(8):
        board.append([])
        for col in range(8):
            board[row].append(None)
    return board


def test_left_white_knight():
    """A simple test for a left white knight."""
    board = setup_empty_board()
    knight = Knight('W', (0, 1))
    is_allowed = knight.step(board, (0, 0))
    print("Is knight B1 allowed to move to A1: " + str(is_allowed))
    is_allowed = knight.step(board, (2, 0))
    print("Is knight B1 allowed to move to C3: " + str(is_allowed))


def test_black_pawn():
    """A simple test for a black pawn."""
    board = setup_empty_board()
    pawn = Pawn('B', (6, 4))
    is_allowed = pawn.step(board, (6, 4))
    print("Is pawn E7 allowed to move to E7: " + str(is_allowed))


test_left_white_knight()
test_black_pawn()
