from a_main_figure import Figure


class Rook(Figure):
    __COUNT = 2
    __PLACES = {'white': ('B', 1), 'black': ('B', 2)}

    __slots__ = ('name', 'current_place')

    def __init__(self, color):
        super().__init__(color=color,
                         default_places=self.__PLACES[color],
                         figure_type_cnt=self.__COUNT)
        self.name = 'Rook'
        self.color = color
        self.current_place = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_color(self):
        return self.color

    def get_current_position(self, chess_id: int = None) -> tuple:
        return ()

    def get_default_position(self, color) -> tuple:
        return self.__PLACES[color]
