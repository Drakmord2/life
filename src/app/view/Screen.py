
import pygame
import config as cfg


class Screen:
    def __init__(self, window):
        self._window = window
        self._font = None

    def showtext(self, win, pos, text, color, bgcolor):
        textimg = self._font.render(text, 1, color, bgcolor)
        win.blit(textimg, pos)

        return pos[0] + textimg.get_width() + 5, pos[1]

    def showHeader(self, generation):
        background = cfg.render['white']
        self._window.fill(background)

        header_position = (0, 0, cfg.render['width'], 50)
        header_color = cfg.render['grey']
        self._window.fill(header_color, header_position)

        self._font = pygame.font.Font(None, 26)
        title_position = (10, 10)
        self._window.blit(self._font.render('Game of Life', 1, cfg.render['white'], cfg.render['grey']), title_position)

        self._font = pygame.font.Font(None, 20)
        generation_position = ((cfg.render['width']/2 + 40), 30)
        generation_fg = cfg.render['white']
        generation_bg = cfg.render['grey']
        pos = self.showtext(self._window, generation_position, 'Generation:', generation_fg, generation_bg)

        gen_num = str(generation)
        self.showtext(self._window, pos, gen_num, cfg.render['white'], cfg.render['grey'])

    def showCells(self, cells):
        for cell in cells:
            surface, rect = cell.get_cell()
            self._window.blit(surface, rect)

        pygame.display.flip()
