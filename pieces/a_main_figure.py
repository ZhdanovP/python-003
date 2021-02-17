from abc import ABCMeta, abstractmethod


class Figure(object):
    __metaclass__ = ABCMeta
    __slots__ = ('color', 'default_places', 'figure_type_cnt')

    @abstractmethod
    def __init__(self,
                 color: any,
                 default_places: tuple,
                 figure_type_cnt: int):
        """
        :param color: in format in:
            'black': Any value that returns negative check result
            'white': Any value that returns positive check result
        :param default_places:
            default places of chess figures on chess board at start program
        :param figure_type_cnt:
            overall count that figure can have
        """
        self.color = color
        self.figure_type_cnt = figure_type_cnt
        self.default_places = default_places

    @abstractmethod
    def step(self, coordinates: tuple) -> None:
        """
        Trying to move figure to specified coordinates X and Y
        where X is chessboard Letter, and Y is number from 1 to 8
        """
        pass

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def get_current_position(self, chess_id: int) -> tuple:
        """
        :return: current position of figure on field in format:
            {letter}, {number}
        """
        pass

    @abstractmethod
    def get_default_position(self, color: str) -> tuple:
        """
        :return: default position of figure on field in format:
            {letter}, {number}
        """
        pass
