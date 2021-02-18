"""The module "chess" implements the game of chess in the console"""

from chess.server.board import ChessBoard, GT_CHESS, GT_CHECKERS


class Game:
    def __init__(self):
        __slots__ = ("_game_type", "_board")

        self._game_type = GT_CHESS
        self._board = ChessBoard()

    def new_game(self, game_type=GT_CHESS):
        self._game_type = game_type
        self._board.new_game()
        print("Enter 'q' to close chess")

        while True:
            print(
                "=====================================================================================================")
            print("")
            print(self._board.bord_draw())
            print("")

            move_data = input("Please type figure finish position to move (example 'a1 or 'g7): ")
            if move_data.lower() == 'q':
                exit()

            self._board.make_move(move_data)


if __name__ == "__main__":
    game_type = GT_CHESS
    while True:
        game_type = int(input("Please choose the type of game (chess - 0, checkers - 1): "))

        if game_type in range(GT_CHESS, GT_CHECKERS+1):
            break
        else:
            print("Please enter valid game type (chess - 0, checkers - 1)")

    Game().new_game(game_type)
