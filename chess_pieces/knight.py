"""Contains a single `Knight` class which represents a knight on a chess board."""

from .chess_piece import ChessPiece


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
