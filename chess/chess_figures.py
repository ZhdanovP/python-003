from abc import ABCMeta, abstractmethod


class Figure(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, color, default_position):
        """
        :param color: in format in:
            'black': Any value that returns negative check result
            'white': Any value that returns positive check result
        """
        self.color = color
        self.default_position = default_position

    @abstractmethod
    def step(self):
        """
        Trying to move figure to specified coordinates X and Y
        where X is chessboard Letter, and Y is number from 1 to 8
        """
        pass

    @abstractmethod
    def get_current_position(self):
        """
        :return: current position of figure on field in format:
            {letter}, {number}
        """
        pass

    @abstractmethod
    def get_default_position(self):
        """
        :return: default position of figure on field in format:
            {letter}, {number}
        """


class Pawn(Figure):

    def __init__(self, color):
        super().__init__(color=color,
                         default_position=('A', 2))
        self.name = 'Pawn'
        self.color = color

    def step(self):
        pass

    def get_current_position(self):
        pass

    def get_default_position(self):
        pass


class Rook(Figure):
    def __init__(self, color):
        super().__init__(color=color, default_position=('B', 2))
        self.name = 'Rook'
        self.color = color

    def step(self):
        pass

    def get_current_position(self):
        pass

    def get_default_position(self):
        pass


class Knight(Figure):
    def __init__(self, color):
        super().__init__(color=color, default_position=('C', 2))
        self.name = 'Knight'
        self.color = color

    def step(self):
        pass

    def get_current_position(self):
        pass

    def get_default_position(self):
        pass


class Bishop(Figure):
    def __init__(self, color):
        super().__init__(color=color, default_position=('D', 2))
        self.name = 'Bishop'
        self.color = color

    def step(self):
        pass

    def get_current_position(self):
        pass

    def get_default_position(self):
        pass


class King(Figure):
    def __init__(self, color):
        super().__init__(color=color, default_position=('E', 2))
        self.name = 'King'
        self.color = color

    def step(self):
        pass

    def get_current_position(self):
        pass

    def get_default_position(self):
        pass


class Queen(Figure):
    def __init__(self, color):
        super().__init__(color=color, default_position=('F', 2))
        self.name = 'Queen'
        self.color = color

    def step(self):
        pass

    def get_current_position(self):
        pass

    def get_default_position(self):
        pass
