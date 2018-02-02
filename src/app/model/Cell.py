
import pygame
import config as cfg


class Cell:

    def __init__(self, position, color=cfg.render['red']):
        self.position = position
        self.color = color

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

    def grid_to_pixels(self):
        i, j = self.position

        xpos = i * 10 + 10
        ypos = j * 10 + 60

        return xpos, ypos
