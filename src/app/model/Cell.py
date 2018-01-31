
import pygame
import config as cfg


class Cell:

    def __init__(self, position, color=cfg.render['black']):
        self.position = position
        self.color = color

    def get_cell(self):
        surface_size = (10, 10)
        surface = pygame.Surface(surface_size)
        surface.fill(self.color)

        cell = pygame.Rect(self.position, (20, 20))

        return surface, cell
