from a_main_figure import Figure


class Bishop(Figure):
    __COUNT = 2
    __PLACES = {'white': (('C', 1), ('F', 1)), 'black': (('C', 8), ('F', 8))}

    __slots__ = ('color', 'name', 'current_pos')

    def __init__(self, color):
        super().__init__(color=color,
                         default_places=self.__PLACES[color],
                         figure_type_cnt=self.__COUNT)
        self.name = 'Bishop'
        self.color = color
        self.current_pos = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_current_position(self, chess_id: int = None) -> tuple:
        return ()

    def get_default_position(self, color) -> tuple:
        return self.__PLACES[color]
