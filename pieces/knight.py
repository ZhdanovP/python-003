import a_main_figure


class Knight(a_main_figure.Figure):
    __COUNT = 2
    __PLACES = (('C', 1), ('C', 2))

    __slots__ = ('color', 'name', 'current_pos')

    def __init__(self, color):
        super().__init__(color=color,
                         default_places=self.__PLACES,
                         figure_type_cnt=self.__COUNT)
        self.name = 'Knight'
        self.color = color
        self.current_pos = self.get_current_position()

    def step(self, coordinates: tuple):
        pass

    def get_current_position(self, chess_id: int = None) -> tuple:
        return ()

    def get_default_position(self, color) -> tuple:
        return self.__PLACES[color]
