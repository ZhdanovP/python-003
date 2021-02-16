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
    def step(self, coordinates: tuple):
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
    __slots__ = ('color', 'name', 'current_pos')

    def __init__(self, color):
        super().__init__(color=color,
                         default_position=('A', 2))
        self.name = 'Pawn'
        self.color = color
        self.current_pos = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_current_position(self) -> tuple:
        pass

    def get_default_position(self) -> tuple:
        pass


class Rook(Figure):
    __slots__ = ('color', 'name', 'current_pos')

    def __init__(self, color):
        super().__init__(color=color, default_position=('B', 2))
        self.name = 'Rook'
        self.color = color
        self.current_pos = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_current_position(self) -> tuple:
        pass

    def get_default_position(self) -> tuple:
        pass


class Knight(Figure):
    __slots__ = ('color', 'name', 'current_pos')

    def __init__(self, color):
        super().__init__(color=color, default_position=('C', 2))
        self.name = 'Knight'
        self.color = color
        self.current_pos = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_current_position(self) -> tuple:
        pass

    def get_default_position(self) -> tuple:
        pass


class Bishop(Figure):
    __slots__ = ('color', 'name', 'current_pos')

    def __init__(self, color):
        super().__init__(color=color, default_position=('D', 2))
        self.name = 'Bishop'
        self.color = color
        self.current_pos = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_current_position(self) -> tuple:
        pass

    def get_default_position(self) -> tuple:
        pass


class King(Figure):
    __slots__ = ('color', 'name', 'current_pos')

    def __init__(self, color):
        super().__init__(color=color, default_position=('E', 2))
        self.name = 'King'
        self.color = color
        self.current_pos = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_current_position(self) -> tuple:
        pass

    def get_default_position(self) -> tuple:
        pass


class Queen(Figure):
    COUNT = 2
    PLACES = (('A', 1), ('A', 2))

    __slots__ = ('name', 'current_place')

    def __init__(self, color=None):
        super().__init__(color='white' if color else 'black',
                         default_places=self.PLACES,
                         figure_type_cnt=self.COUNT)
        self.name = 'Queen'
        self.current_place = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_current_position(self, id_: int = None) -> tuple:
        return 'A', 5

    def get_default_position(self, id_: int) -> tuple:
        pass


x = Queen(1)
y = Queen()
z = 1
