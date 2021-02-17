from a_main_figure import Figure


class Queen(Figure):
    __COUNT = 1
    __PLACES = {'white': ('E', 1), 'black': ('E', 8)}

    __slots__ = ('name', 'current_place')

    def __init__(self, color=None):
        super().__init__(color='white' if color else 'black',
                         default_places=self.__PLACES[color],
                         figure_type_cnt=self.__COUNT)
        self.name = 'Queen'
        self.current_place = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_current_position(self, chess_id: int = None) -> tuple:
        return ()

    def get_default_position(self, color) -> tuple:
        return self.__PLACES[color]
