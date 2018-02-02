
import random
from model.Cell import Cell


class CellController:

    def __init__(self, ci):
        self.ci = ci

    def generate(self):
        cells = []
        num_cells = random.randrange(10, 30)

        for i in range(0, num_cells):
            x = random.randrange(1, 30)
            y = random.randrange(1, 25)

            cell_position = self.get_pos(x, y)
            cell = Cell(cell_position)

            cells.append(cell)

        return cells

    def get_pos(self, x, y):
        xpos = x * 10 + 10
        ypos = y * 10 + 60

        return xpos, ypos
