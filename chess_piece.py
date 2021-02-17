from abc import ABC, abstractmethod


class ChessPiece(ABC):
    """The base class for chess figures"""
    __slots__ = ['color']

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

    @abstractmethod
    def get_all_possible_moves(self, board):
        return NotImplemented

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
