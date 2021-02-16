"""A simple chess piece algorithms."""


class ChessPiece:
    """The base class for chess figures"""

    def __init__(self, color, position):
        """
        Creates a chess piece of a given color and places it into a specified position.
        :param color: A color of a piece, could be 'W' or 'B'.
        :param position: A tuple describing a position of a piece in a form (row, col), e.g. E2 is (1, 4).
        """
        self.color = color
        self.position = position

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def step(self, board, possible_move):
        """
        Checks if a given move possible in a given board.
        :param board: A chess board to check on.
        :param possible_move: A move to check.
        :return: True if a given move is possible, False otherwise.
        """
        all_moves = self.get_all_possible_moves(board)
        return possible_move in all_moves

    def get_all_possible_moves(self, board):
        return []

    def perform_move(self, board, move):
        """
        Moves a piece instance to a given new position.
        :param board: A board where movement is performed.
        :param move: A new position for a piece in the form of (row, col).
        """
        if board[move[0]][move[1]] is not None:
            self.been_adversary = False
        board[move[0]][move[1]] = self
        board[self.position[0]][self.position[1]] = None
        self.position = move

    def in_bounds(self, board, new_pos):
        """
        Return True only if 'new_pos' is not occupied or occupied by an
        adversary. Additionally, the previous position sent to 'in_bounds'
        must not have contained an adversary.
        :param board: A chess board.
        :param new_pos: A position to check.
        """
        if self.been_adversary:
            self.been_adversary = False
            return False

        # make sure 'new_pos' in inside the board
        if new_pos[0] < 0 or new_pos[1] < 0:
            return False
        try:
            item = board[new_pos[0]][new_pos[1]]
            # An item can only be an adversary.
            if item is None:
                return True
            elif item.get_color() == self.get_color():
                return False
            elif item.get_color() != self.get_color:
                self.been_adversary = True
                return True
            else:
                return True
        except:
            return False

    def __str__(self):
        return self.color

    position = ()

    # The previous position sent to in_bounds was an adversary.
    been_adversary = False


class Knight(ChessPiece):
    """
    Represents a knight on a chess board.
    """
    def __init__(self, color, position):
        super(Knight, self).__init__(color, position)

    def get_all_possible_moves(self, board):
        """
        Returns all possible moves of this Knight instance for a given chess board.
        :param board: A chess board to check on.
        :return: All possible moves of this Knight instance.
        """
        moves = []
        my_pos = super(Knight, self).get_position()

        for i in range(-2, 3, 1):
            for j in range(-2, 3, 1):
                if (abs(i) == 1 and abs(j) == 2) or (abs(i) == 2 and abs(j) == 1):
                    new_pos = (my_pos[0] + i, my_pos[1] + j)
                    if super(Knight, self).in_bounds(board, new_pos):
                        moves.append(new_pos)
        return moves

    def __str__(self):
        return 'Knight' + super(Knight, self).__str__()


class Pawn(ChessPiece):
    """
    Represents a pawn on a chess board.
    """
    is_first_move = True
    color = ''

    def __init__(self, position, color):
        """
        Preconditions:
            position must be a tuple in the format (row, col)
            color must be a String that is either 'White' or 'Black'
        """
        super(Pawn, self).__init__(position, color)
        self.color = color
        self.pos = position

    def get_all_possible_moves(self, board):
        """
        Returns all possible moves of this Pawn instance for a given chess board.
        :param board: A chess board to check on.
        :return: All possible moves of this Pawn instance.
        """
        moves = []
        my_pos = super(Pawn, self).get_position()
        if self.color == 'White':
            if self.is_first_move:
                self.is_first_move = False
                new_pos = (my_pos[0] - 2, my_pos[1])
                if super(Pawn, self).in_bounds(board, new_pos):
                    moves.append(new_pos)
            new_pos = (my_pos[0] - 1, my_pos[1])
            if super(Pawn, self).in_bounds(board, new_pos):
                moves.append(new_pos)
        else:
            if self.is_first_move:
                self.is_first_move = False
                new_pos = (my_pos[0] + 2, my_pos[1])
                if super(Pawn, self).in_bounds(board, new_pos):
                    moves.append(new_pos)
            new_pos = (my_pos[0] + 1, my_pos[1])
            if super(Pawn, self).in_bounds(board, new_pos):
                moves.append(new_pos)

        return moves

    def __str__(self):
        return 'Pawn' + super(Pawn, self).__str__()


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
