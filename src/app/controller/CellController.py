
import random
import config as cfg
from model.Cell import Cell
from view.Screen import Screen

screen = Screen(None)
padding = 10


class CellController:

    def __init__(self):
        pass

    def generate(self):
        cells = []
        num_cells = random.randrange(1, 11)

        for i in range(0, num_cells):
            xfrom = padding
            xto = cfg.render['width'] - padding
            posx = random.randrange(xfrom, xto)

            yfrom = padding + cfg.render['header_height']
            yto = cfg.render['height'] - padding
            posy = random.randrange(yfrom, yto)

            cell_position = (posx, posy)
            cell_color = screen.random_color()
            cell = Cell(cell_position, cell_color)

            cells.append(cell)

        return cells
