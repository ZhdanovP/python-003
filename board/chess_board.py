from abc import ABCMeta, abstractmethod


class ChessField(ABCMeta):

    @abstractmethod
    def get_figure(cls, figure):
        """
        :returns chess name and color on specified place
        by coordinates X nd Y
        where X is chessboard Letter, and Y is number from 1 to 8
        """
        pass
