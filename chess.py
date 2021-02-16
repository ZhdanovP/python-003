import random
from sys import stdout
from termcolor import colored

board_x_min = 0
board_y_min = 0
board_x_max = 7
board_y_max = 7

_figuresMatrix = [[None for i in range(8)] for j in range(8)]

def isFreeCell(x, y):
	return None == _figuresMatrix[x][y]
def setCellFigure(x, y, obj):
	_figuresMatrix[x][y] = obj
def getCellFigure(x, y):
	return _figuresMatrix[x][y]
def resetCell(x, y):
	_figuresMatrix[x][y] = None

def LitPos2DecPos(LitPos):
	Literas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	index = Literas.index(LitPos)
	return index
	pass

class Position():
	_mX = 0
	_mY = 0
	def __init__(self, x, y):
		self._mX = x
		self._mY = y
	def getX(self):
		return self._mX
	def getY(self):
		return self._mY

class Peshka():
	_isWhite = False
	_pos_x = 0
	_pos_y = 0
	def __init__(self, isWhite):
		# print("Peshka cstor: isWhite=" + str(isWhite))
		self._isWhite = isWhite
	def setX(self, x):
		self._pos_x = x
	def setY(self, y):
		self._pos_y = y
	def getX(self):
		return self._pos_x
	def getY(self):
		return self._pos_y
	def isWhite(self):
		return self._isWhite

	def getAvailableCells(self):
		steps = []
		if(self._isWhite):
			if((self._pos_y + 1) <= board_y_max):
				if(isFreeCell(self._pos_x, self._pos_y + 1)):
					pos_new = Position(self._pos_x, self._pos_y + 1)
					steps.append(pos_new)
			if((self._pos_y + 2) <= board_y_max):
				if(isFreeCell(self._pos_x, self._pos_y + 2)):
					pos_new = Position(self._pos_x, self._pos_y + 2)
					steps.append(pos_new)
		else:
			if((self._pos_y - 1) >= board_y_min):
				if(isFreeCell(self._pos_x, self._pos_y - 1)):
					pos_new = Position(self._pos_x, self._pos_y - 1)
					steps.append(pos_new)
			if((self._pos_y - 2) >= board_y_min):
				if(isFreeCell(self._pos_x, self._pos_y - 2)):
					pos_new = Position(self._pos_x, self._pos_y - 2)
					steps.append(pos_new)

		return steps

class Knight():
	_isWhite = False
	_pos_x = 0
	_pos_y = 0
	def __init__(self, isWhite):
		# print("Knight cstor")
		self._isWhite = isWhite

	def setX(self, x):
		self._pos_x = x
	def setY(self, y):
		self._pos_y = y
	def getX(self):
		return self._pos_x
	def getY(self):
		return self._pos_y
	def isWhite(self):
		return self._isWhite

	def getAvailableCells(self):
		steps = []
		pos_x_new = self._pos_x + 2
		pos_y_new = self._pos_y + 1
		if(pos_x_new <= board_x_max and pos_y_new <= board_y_max):
			if(isFreeCell(pos_x_new, pos_y_new)):
				pos_new = Position(pos_x_new, pos_y_new)
				steps.append(pos_new)

		pos_x_new = self._pos_x + 2
		pos_y_new = self._pos_y - 1
		if(pos_x_new <= board_x_max and pos_y_new >= board_y_min):
			if(isFreeCell(pos_x_new, pos_y_new)):
				pos_new = Position(pos_x_new, pos_y_new)
				steps.append(pos_new)

		pos_x_new = self._pos_x - 2
		pos_y_new = self._pos_y + 1
		if(pos_x_new >= board_x_min and pos_y_new <= board_y_max):
			if(isFreeCell(pos_x_new, pos_y_new)):
				pos_new = Position(pos_x_new, pos_y_new)
				steps.append(pos_new)

		pos_x_new = self._pos_x - 2
		pos_y_new = self._pos_y - 1
		if(pos_x_new >= board_x_min and pos_y_new >= board_y_min):
			if(isFreeCell(pos_x_new, pos_y_new)):
				pos_new = Position(pos_x_new, pos_y_new)
				steps.append(pos_new)

		pos_x_new = self._pos_x + 1
		pos_y_new = self._pos_y + 2
		if(pos_x_new <= board_x_max and pos_y_new <= board_y_max):
			if(isFreeCell(pos_x_new, pos_y_new)):
				pos_new = Position(pos_x_new, pos_y_new)
				steps.append(pos_new)

		pos_x_new = self._pos_x + 1
		pos_y_new = self._pos_y - 2
		if(pos_x_new <= board_x_max and pos_y_new >= board_y_min):
			if(isFreeCell(pos_x_new, pos_y_new)):
				pos_new = Position(pos_x_new, pos_y_new)
				steps.append(pos_new)

		pos_x_new = self._pos_x - 1
		pos_y_new = self._pos_y + 2
		if(pos_x_new >= board_x_min and pos_y_new <= board_y_max):
			if(isFreeCell(pos_x_new, pos_y_new)):
				pos_new = Position(pos_x_new, pos_y_new)
				steps.append(pos_new)

		pos_x_new = self._pos_x - 1
		pos_y_new = self._pos_y - 2
		if(pos_x_new >= board_x_min and pos_y_new >= board_y_min):
			if(isFreeCell(pos_x_new, pos_y_new)):
				pos_new = Position(pos_x_new, pos_y_new)
				steps.append(pos_new)

		return steps

class Bishop():
	_isWhite = False
	_pos_x = 0
	_pos_y = 0
	def __init__(self, isWhite):
		# print("Bishop cstor:")
		self._isWhite = isWhite

	def setX(self, x):
		self._pos_x = x
	def setY(self, y):
		self._pos_y = y
	def getX(self):
		return self._pos_x
	def getY(self):
		return self._pos_y
	def isWhite(self):
		return self._isWhite

	def getAvailableCells(self):
		steps = []
		dXY = 1
		for x in range(self._pos_x - 1, board_x_min, -1):
			pos_x_new = self._pos_x + dXY
			pos_y_new = self._pos_y + dXY
			if(pos_x_new <= board_x_max and pos_y_new <= board_y_max):
				if(isFreeCell(pos_x_new, pos_y_new)):
					pos_new = Position(pos_x_new, pos_y_new)
					steps.append(pos_new)
					++dXY
				else:
					break;
			else:
				break;
		dXY = 1
		for x in range(self._pos_x + 1, board_x_max, 1):
			pos_x_new = self._pos_x - dXY
			pos_y_new = self._pos_y - dXY
			if(pos_x_new >= board_x_min and pos_y_new >= board_y_min):
				if(isFreeCell(pos_x_new, pos_y_new)):
					pos_new = Position(pos_x_new, pos_y_new)
					steps.append(pos_new)
					++dXY
				else:
					break;
			else:
				break;
		dXY = 1
		for x in range(self._pos_x - 1, board_x_min, -1):
			pos_x_new = self._pos_x + dXY
			pos_y_new = self._pos_y - dXY
			if(pos_x_new <= board_x_max and pos_y_new >= board_y_min):
				if(isFreeCell(pos_x_new, pos_y_new)):
					pos_new = Position(pos_x_new, pos_y_new)
					steps.append(pos_new)
					++dXY
				else:
					break;
			else:
				break;
		dXY = 1
		for x in range(self._pos_x + 1, board_x_max, 1):
			pos_x_new = self._pos_x - dXY
			pos_y_new = self._pos_y + dXY
			if(pos_x_new >= board_x_min and pos_y_new <= board_y_max):
				if(isFreeCell(pos_x_new, pos_y_new)):
					pos_new = Position(pos_x_new, pos_y_new)
					steps.append(pos_new)
					++dXY
				else:
					break;
			else:
				break;

		return steps

class Rook():
	_isWhite = False
	_pos_x = 0
	_pos_y = 0
	def __init__(self, isWhite):
		# print("Rook cstor:")
		self._isWhite = isWhite

	def setX(self, x):
		self._pos_x = x
	def setY(self, y):
		self._pos_y = y
	def getX(self):
		return self._pos_x
	def getY(self):
		return self._pos_y
	def isWhite(self):
		return self._isWhite

	def getAvailableCells(self):
		steps = []
		dXY = 1
		for x in range(self._pos_x + 1, board_x_max, 1):
			pos_x_new = self._pos_x + dXY
			pos_y_new = self._pos_y
			if(pos_x_new <= board_x_max):
				if(isFreeCell(pos_x_new, pos_y_new)):
					pos_new = Position(pos_x_new, self._pos_y)
					steps.append(pos_new)
					++dXY
				else:
					break;
			else:
				break;
		dXY = 1
		for x in range(self._pos_x - 1, board_x_min, -1):
			pos_x_new = self._pos_x - dXY
			pos_y_new = self._pos_y
			if(pos_x_new >= board_x_min):
				if(isFreeCell(pos_x_new, pos_y_new)):
					pos_new = Position(pos_x_new, pos_y_new)
					steps.append(pos_new)
					++dXY
			else:
				break;
		dXY = 1
		for x in range(self._pos_y + 1, board_y_max, 1):
			pos_x_new = self._pos_x
			pos_y_new = self._pos_y + dXY
			if(pos_y_new >= board_y_max):
				if(isFreeCell(pos_x_new, pos_y_new)):
					pos_new = Position(pos_x_new, pos_y_new)
					steps.append(pos_new)
					++dXY
				else:
					break;
			else:
				break;
		dXY = 1
		for x in range(self._pos_y - 1, board_y_min, -1):
			pos_x_new = self._pos_x
			pos_y_new = self._pos_y - dXY
			if(pos_y_new >= board_y_min):
				if(isFreeCell(pos_x_new, pos_y_new)):
					pos_new = Position(pos_x_new, pos_y_new)
					steps.append(pos_new)
					++dXY
				else:
					break;
			else:
				break;

		return steps

class Queen():
	_isWhite = False
	_pos_x = 0
	_pos_y = 0
	def __init__(self, isWhite):
		# print("Queen cstor:")
		self._isWhite = isWhite

	def setX(self, x):
		self._pos_x = x
	def setY(self, y):
		self._pos_y = y
	def getX(self):
		return self._pos_x
	def getY(self):
		return self._pos_y
	def isWhite(self):
		return self._isWhite

	def getAvailableCells(self):
		steps = []
		bishop = Bishop(self._isWhite)
		bishop.setX(self._pos_x)
		bishop.setY(self._pos_y)
		rook = Rook(self._isWhite)
		rook.setX(self._pos_x)
		rook.setY(self._pos_y)
		steps.extend(bishop.getAvailableCells())
		steps.extend(rook.getAvailableCells())

		return steps;

class King():
	_isWhite = False
	_pos_x = 0
	_pos_y = 0
	def __init__(self, isWhite):
		# print("King cstor:")
		self._isWhite = isWhite

	def setX(self, x):
		self._pos_x = x
	def setY(self, y):
		self._pos_y = y
	def getX(self):
		return self._pos_x
	def getY(self):
		return self._pos_y
	def isWhite(self):
		return self._isWhite

	def getAvailableCells(self):
		steps = []
		pos_x_new = self._pos_x + 1
		pos_y_new = self._pos_y
		if(pos_x_new <= board_x_max):
			pos_new = Position(pos_x_new, self._pos_y)
			steps.append(pos_new)

		pos_x_new = self._pos_x - 1
		pos_y_new = self._pos_y
		if(pos_x_new >= board_x_min):
			pos_new = Position(pos_x_new, self._pos_y)
			steps.append(pos_new)

		pos_x_new = self._pos_x
		pos_y_new = self._pos_y + 1
		if(pos_y_new <= board_y_max):
			pos_new = Position(pos_x_new, pos_y_new)
			steps.append(pos_new)

		pos_x_new = self._pos_x
		pos_y_new = self._pos_y - 1
		if(pos_y_new >= board_y_min):
			pos_new = Position(pos_x_new, pos_y_new)
			steps.append(pos_new)

		pos_x_new = self._pos_x + 1
		pos_y_new = self._pos_y + 1
		if(pos_x_new <= board_x_max and pos_y_new <= board_y_max):
			pos_new = Position(pos_x_new , pos_y_new)
			steps.append(pos_new)

		pos_x_new = self._pos_x - 1
		pos_y_new = self._pos_y + 1
		if(pos_x_new >= board_x_min and (pos_y_new) <= board_y_max):
			pos_new = Position(pos_x_new, pos_y_new)
			steps.append(pos_new)

		pos_x_new = self._pos_x + 1
		pos_y_new = self._pos_y - 1
		if(pos_x_new <= board_x_max and (pos_y_new) >= board_y_min):
			pos_new = Position(pos_x_new, pos_y_new)
			steps.append(pos_new)

		pos_x_new = self._pos_x - 1
		pos_y_new = self._pos_y - 1
		if(pos_x_new >= board_x_min and pos_y_new >= board_y_min):
			pos_new = Position(pos_x_new, pos_y_new)
			steps.append(pos_new)

		return steps;

class ChessBoard:
	_figuresList = []
	def __init__(self):
		# print(self.figures)
		# print("ChessBoard cstor")
		self._figuresList = []
		for i in range(0, 8):
			peshka = Peshka(True)
			self._figuresList.append(peshka)
			while True:
				pos_x_new = random.randint(board_x_min, board_x_max)
				pos_y_new = random.randint(board_y_min, board_y_max)

				if(isFreeCell(pos_x_new, pos_y_new)):
					peshka.setX(pos_x_new)
					peshka.setY(pos_y_new)
					setCellFigure(pos_x_new, pos_y_new, peshka)
					break
		for i in range(0, 8):
			peshka = Peshka(False)
			self._figuresList.append(peshka)
			while True:
				pos_x_new = random.randint(board_x_min, board_x_max)
				pos_y_new = random.randint(board_y_min, board_y_max)

				if(isFreeCell(pos_x_new, pos_y_new)):
					peshka.setX(pos_x_new)
					peshka.setY(pos_y_new)
					setCellFigure(pos_x_new, pos_y_new, peshka)
					break
		for i in range(0, 2):
			knight = Knight(True)
			self._figuresList.append(knight)
			while True:
				pos_x_new = random.randint(board_x_min, board_x_max)
				pos_y_new = random.randint(board_y_min, board_y_max)

				if(isFreeCell(pos_x_new, pos_y_new)):
					knight.setX(pos_x_new)
					knight.setY(pos_y_new)
					setCellFigure(pos_x_new, pos_y_new, knight)
					break
		for i in range(0, 2):
			knight = Knight(False)
			self._figuresList.append(knight)
			while True:
				pos_x_new = random.randint(board_x_min, board_x_max)
				pos_y_new = random.randint(board_y_min, board_y_max)

				if(isFreeCell(pos_x_new, pos_y_new)):
					knight.setX(pos_x_new)
					knight.setY(pos_y_new)
					setCellFigure(pos_x_new, pos_y_new, knight)
					break
		for i in range(0, 2):
			bishop = Bishop(True)
			self._figuresList.append(bishop)
			while True:
				pos_x_new = random.randint(board_x_min, board_x_max)
				pos_y_new = random.randint(board_y_min, board_y_max)

				if(isFreeCell(pos_x_new, pos_y_new)):
					bishop.setX(pos_x_new)
					bishop.setY(pos_y_new)
					setCellFigure(pos_x_new, pos_y_new, bishop)
					break
		for i in range(0, 2):
			bishop = Bishop(False)
			self._figuresList.append(bishop)
			while True:
				pos_x_new = random.randint(board_x_min, board_x_max)
				pos_y_new = random.randint(board_y_min, board_y_max)

				if(isFreeCell(pos_x_new, pos_y_new)):
					bishop.setX(pos_x_new)
					bishop.setY(pos_y_new)
					setCellFigure(pos_x_new, pos_y_new, bishop)
					break
		for i in range(0, 2):
			rook = Rook(True)
			self._figuresList.append(rook)
			while True:
				pos_x_new = random.randint(board_x_min, board_x_max)
				pos_y_new = random.randint(board_y_min, board_y_max)

				if(isFreeCell(pos_x_new, pos_y_new)):
					rook.setX(pos_x_new)
					rook.setY(pos_y_new)
					setCellFigure(pos_x_new, pos_y_new, rook)
					break;
		for i in range(0, 2):
			rook = Rook(False)
			self._figuresList.append(rook)
			while True:
				pos_x_new = random.randint(board_x_min, board_x_max)
				pos_y_new = random.randint(board_y_min, board_y_max)

				if(isFreeCell(pos_x_new, pos_y_new)):
					rook.setX(pos_x_new)
					rook.setY(pos_y_new)
					setCellFigure(pos_x_new, pos_y_new, rook)
					break;
		queen = Queen(True)
		self._figuresList.append(queen)
		while True:
			pos_x_new = random.randint(board_x_min, board_x_max)
			pos_y_new = random.randint(board_y_min, board_y_max)

			if(isFreeCell(pos_x_new, pos_y_new)):
				queen.setX(pos_x_new)
				queen.setY(pos_y_new)
				setCellFigure(pos_x_new, pos_y_new, queen)
				break;
		queen = Queen(False)
		self._figuresList.append(queen)
		while True:
			pos_x_new = random.randint(board_x_min, board_x_max)
			pos_y_new = random.randint(board_y_min, board_y_max)

			if(isFreeCell(pos_x_new, pos_y_new)):
				queen.setX(pos_x_new)
				queen.setY(pos_y_new)
				setCellFigure(pos_x_new, pos_y_new, queen)
				break;
		king = King(True)
		self._figuresList.append(king)
		while True:
			pos_x_new = random.randint(board_x_min, board_x_max)
			pos_y_new = random.randint(board_y_min, board_y_max)

			if(isFreeCell(pos_x_new, pos_y_new)):
				king.setX(pos_x_new)
				king.setY(pos_y_new)
				setCellFigure(pos_x_new, pos_y_new, king)
				break;
		king = King(False)
		self._figuresList.append(king)
		while True:
			pos_x_new = random.randint(board_x_min, board_x_max)
			pos_y_new = random.randint(board_y_min, board_y_max)

			if(isFreeCell(pos_x_new, pos_y_new)):
				king.setX(pos_x_new)
				king.setY(pos_y_new)
				setCellFigure(pos_x_new, pos_y_new, king)
				break;
	def step(self):
		for figure in self._figuresList:
			pos_x_old = figure.getX()
			pos_y_old = figure.getY()
			cells = figure.getAvailableCells()
			for cell in cells:
				if(isFreeCell(cell.getX(), cell.getY())):
					print("move " + str(type(getCellFigure(pos_x_old, pos_y_old)).__name__) + " from " + str(pos_x_old) + "x" + str(pos_y_old) + 
						" to " + str(cell.getX()) + "x" + str(cell.getY()))
					figure.setX(cell.getX())
					figure.setY(cell.getY())
					resetCell(pos_x_old, pos_y_old)
					setCellFigure(cell.getX(), cell.getY(), figure)
					break
	def print(self):
		print(" ", end = "")
		for x in range(board_x_min, board_x_max + 1, 1):
			print(" " + str(x), end = "")
		print("")
		for y in range(board_y_min, board_y_max + 1, 1):
			print(str(y) + "|", end = "")
			for x in range(board_x_min, board_x_max + 1, 1):
				if(Peshka == type(getCellFigure(x, y))):
					if(False == getCellFigure(x, y).isWhite()):
						print(colored("p", 'grey'), end = "")
					else:
						print(colored("p", 'white'), end = "")
				elif(Knight == type(getCellFigure(x, y))):
					if(False == getCellFigure(x, y).isWhite()):
						print(colored("k", 'grey'), end = "")
					else:
						print(colored("k", 'white'), end = "")
				elif(Bishop == type(getCellFigure(x, y))):
					if(False == getCellFigure(x, y).isWhite()):
						print(colored("b", 'grey'), end = "")
					else:
						print(colored("b", 'white'), end = "")
				elif(Rook == type(getCellFigure(x, y))):
					if(False == getCellFigure(x, y).isWhite()):
						print(colored("r", 'grey'), end = "")
					else:
						print(colored("r", 'white'), end = "")
				elif(Queen == type(getCellFigure(x, y))):
					if(False == getCellFigure(x, y).isWhite()):
						print(colored("Q", 'grey'), end = "")
					else:
						print(colored("Q", 'white'), end = "")
				elif(King == type(getCellFigure(x, y))):
					if(False == getCellFigure(x, y).isWhite()):
						print(colored("K", 'grey'), end = "")
					else:
						print(colored("K", 'white'), end = "")
				else:
					print(" ", end = "")
				print("|", end = "")
			stdout.write("\n")
		

def main():
	board = ChessBoard()

	print("Initial state")
	print("")
	board.print()
	for i in range(1, 2):
		print("")
		print("Step " + str(i))
		print("")
		board.step()
		board.print()

if __name__ == "__main__":
	main()
