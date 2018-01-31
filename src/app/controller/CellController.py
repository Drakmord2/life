
import random
import config as cfg
from model.Cell import Cell


class CellController:

    def __init__(self):
        pass

    def generate(self):
        cells = []
        num_cells = random.randrange(1, 11)

        for i in range(0, num_cells):
            posx = random.randrange(10, cfg.render['width']-10)
            posy = random.randrange(10, cfg.render['height']-10)

            cell_position = (posx, posy)
            cell = Cell(cell_position)

            cells.append(cell)

        return cells

