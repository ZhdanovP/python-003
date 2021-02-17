from abc import ABC, abstractmethod
class ChessPiece(ABC):
    def draw(self):
        """Base method for all childs."""
    print("Drew a chess piece")

    @abstractmethod
        def move(self):
        """Abstract method"""
    pass

a = ChessPiecce() # is disallowed


#see also DECORATORS.
