
import pygame
from ..config import cfg


class Cell(object):

    def __init__(self, position, alive=True, color=cfg.render['red']):
        self.position = position
        self.color = color
        self.alive = alive

    def get_cell(self):
        surface_size = (10, 10)
        surface = pygame.Surface(surface_size)
        surface.fill(self.color)

        cell = pygame.Rect(self.grid_to_pixels(), (20, 20))

        return surface, cell

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def set_color(self, color):
        self.color = color

    def live(self):
        self.alive = True
        self.color = cfg.render['red']

    def dead(self):
        self.alive = False
        self.color = cfg.render['white']

    def grid_to_pixels(self):
        i, j = self.position

        xpos = i * 10 + 10
        ypos = j * 10 + 60

        return xpos, ypos
