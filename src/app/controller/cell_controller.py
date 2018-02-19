
import random
from ..model.cell import Cell


class CellController(object):

    def __init__(self, ci):
        self.ci = ci
        self.cfg = ci.get('config')

    def lifecycle(self, cells):
        new_cells = []
        live_cell_slots = self.get_grid_positions(cells)

        for cell in cells:
            new_cell = cell
            neighbors = self.get_neighbors(cell, live_cell_slots)

            if neighbors < 2 and cell.alive:
                new_cell.dead()
                new_cells.append(new_cell)
                continue

            if neighbors > 3 and cell.alive:
                new_cell.dead()
                new_cells.append(new_cell)
                continue

            if (neighbors == 2 or neighbors == 3) and cell.alive:
                new_cell.live()
                new_cells.append(new_cell)
                continue

            if neighbors == 3 and not cell.alive:
                new_cell.live()
                new_cells.append(new_cell)
                continue

            if neighbors != 3 and not cell.alive:
                new_cell.dead()
                new_cells.append(new_cell)
                continue

        return new_cells

    def get_cells(self):
        cells = []
        positions = []

        min_cells = self.cfg.life['min_cells']
        max_cells = self.cfg.life['max_cells']

        num_cells = random.randrange(min_cells, max_cells)

        rows = self.cfg.render['rows']
        columns = self.cfg.render['columns']

        for i in range(0, num_cells):
            x = random.randrange(0, columns-1)
            y = random.randrange(0, rows-1)

            cell_position = (x, y)

            if cell_position not in positions:
                positions.append(cell_position)

                cell = Cell(cell_position)
                cells.append(cell)

        for i in range(0, columns-1):
            for j in range(0, rows-1):
                dead_pos = (i, j)
                if dead_pos not in positions:
                    positions.append(dead_pos)

                    cell = Cell(dead_pos, False, self.cfg.render['white'])
                    cells.append(cell)

        cells = self.sort_cells(cells)

        return cells

    def create_pattern(self, pattern):
        cells = []
        positions = []

        rows = self.cfg.render['rows']
        columns = self.cfg.render['columns']

        for position in pattern:
            positions.append(position)

            cell = Cell(position)
            cells.append(cell)

        for i in range(0, columns-1):
            for j in range(0, rows-1):
                dead_pos = (i, j)
                if dead_pos not in positions:
                    positions.append(dead_pos)

                    cell = Cell(dead_pos, False, self.cfg.render['white'])
                    cells.append(cell)

        cells = self.sort_cells(cells)

        return cells

    def set_cells(self, positions):
        cells = []

        for position in positions:
            cell = Cell(position)
            cells.append(cell)

        return cells

    def get_neighbors(self, cell, live_cell_slots):
        neighbors = 0
        i, j = cell.get_position()

        slots = [(i-1, j-1), (i, j-1), (i+1, j-1),
                 (i-1, j), (i+1, j),
                 (i-1, j+1), (i, j+1), (i+1, j+1)]

        for s in slots:
            if s in live_cell_slots:
                neighbors += 1

        return neighbors

    def get_grid_positions(self, cells):
        positions = []

        for cell in cells:
            if cell.alive:
                positions.append(cell.get_position())

        return positions

    def sort_cells(self, cells):
        sorted_cells = []

        rows = self.cfg.render['rows']
        columns = self.cfg.render['columns']

        for j in range(0, rows-1):
            for i in range(0, columns-1):
                pos = (i, j)
                for cell in cells:
                    if cell.position == pos:
                        sorted_cells.append(cell)

        return sorted_cells

    def cells_alive(self, cells):
        status = False

        for cell in cells:
            if cell.alive:
                status = True
                break

        return status

    def grid_to_pixels(self, x, y):
        xpos = x * 10 + 10
        ypos = y * 10 + 60

        return xpos, ypos

    def pixels_to_grid(self, xpos, ypos):
        x = xpos / 10 - 10
        y = ypos / 10 - 60

        return x, y
