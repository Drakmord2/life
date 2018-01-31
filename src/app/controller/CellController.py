
import random
from model.Cell import Cell
from model.Board import Board


class CellController:

    def __init__(self):
        pass

    def generate(self):
        cells = []
        num_cells = random.randrange(1, 21)

        for i in range(0, num_cells):
            posx = random.randrange(10, 300)
            posy = random.randrange(10, 230)

            cell_position = (posx, posy)
            cell = Cell(cell_position)

            cells.append(cell)

        return cells

    def manage_board(self, cells, SCREEN_SIZE):
        board = Board(SCREEN_SIZE, cells)
