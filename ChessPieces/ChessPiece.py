from abc import ABC, abstractmethod


class ChessPiece(ABC):
    """Base class for Chess figure"""
    __slots__ = ('pos_x', 'pos_y', 'color', 'step')

    def __init__(self, fig_type, pos_x, pos_y, color):
        self.fig_type = fig_type
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    @abstractmethod
    def step(self, dest_x, dest_y):
        """Abstract method to check if move is possible"""
        pass
