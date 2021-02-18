"""Contains a single `Pawn` class which represents a pawn on a chess board."""

from .chess_piece import ChessPiece


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
