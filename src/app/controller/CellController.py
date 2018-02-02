
# The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is
#  in one of two possible states, alive or dead, or "populated" or "unpopulated". Every cell interacts with its eight
#  neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the
#  following transitions occur:
#
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import random
from model.Cell import Cell


class CellController:

    def __init__(self, ci):
        self.ci = ci

    def lifecycle(self, cells):
        new_cells = cells

        for cell in cells:
            neighbors = self.get_neighbors(cell, cells)

            if neighbors < 2:
                new_cells.remove(cell)

            if neighbors == 2 or neighbors == 3:
                continue

            if neighbors > 3:
                new_cells.remove(cell)

        return new_cells

    def get_cells(self):
        cells = []
        positions = []
        num_cells = random.randrange(10, 30)

        for i in range(0, num_cells):
            x = random.randrange(1, 32)
            y = random.randrange(1, 32)

            cell_position = (x, y)

            if cell_position not in positions:
                positions.append(cell_position)

                cell = Cell(cell_position)
                cells.append(cell)

        return cells

    def create_cell(self, position, cells):
        cell = Cell(position)
        cells.append(cell)

        return cells

    def get_neighbors(self, cell, cells):
        neighbors = 0
        i, j = cell.get_position()

        slots = [(i-1, j-1), (i, j-1), (i+1, j-1),
                 (i-1, j), (i+1, j),
                 (i-1, j+1), (i, j+1), (i+1, j+1)]

        cell_slots = self.get_grid_positions(cells)

        for s in slots:
            if s in cell_slots:
                neighbors += 1

        return neighbors

    def get_grid_positions(self, cells):
        positions = []

        for cell in cells:
            positions.append(cell.get_position())

        return positions

    def grid_to_pixels(self, x, y):
        xpos = x * 10 + 10
        ypos = y * 10 + 60

        return xpos, ypos

    def pixels_to_grid(self, xpos, ypos):
        x = xpos / 10 - 10
        y = ypos / 10 - 60

        return x, y
