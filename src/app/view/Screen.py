
import random
import pygame
import config as cfg


class Screen:
    def __init__(self, window):
        self._window = window
        self._font = None

    def main(self):
        header_position = (0, 0, cfg.render['width'], cfg.render['height'])
        header_color = cfg.render['grey']
        self._window.fill(header_color, header_position)

        self._font = pygame.font.Font(None, 42)
        title_position = (65, 50)
        self._window.blit(self._font.render('Game of Life', 1, cfg.render['white'], cfg.render['grey']), title_position)

        block_position = (30, 140, 270, 85)
        block_color = cfg.render['white']
        self._window.fill(block_color, block_position)

        self._font = pygame.font.Font(None, 20)
        msg_position = (50, 160)
        msg_fg = cfg.render['black']
        msg_bg = cfg.render['white']
        msg = 'Scroll down to start a random game'
        self.show_text(self._window, msg_position, msg, msg_fg, msg_bg)

        msg_position = (70, 190)
        msg2 = 'Scroll up to create a pattern'
        self.show_text(self._window, msg_position, msg2, msg_fg, msg_bg)

        footer_position = (110, 300)
        footer = '© Drakmord2'
        self.show_text(self._window, footer_position, footer, cfg.render['white'], cfg.render['grey'])

        pygame.display.flip()

    def show_text(self, win, pos, text, color, bgcolor):
        textimg = self._font.render(text, 1, color, bgcolor)
        win.blit(textimg, pos)

        return pos[0] + textimg.get_width() + 5, pos[1]

    def show_header(self, generation):
        header_position = (0, 0, cfg.render['width'], 50)
        header_color = cfg.render['grey']
        self._window.fill(header_color, header_position)

        self._font = pygame.font.Font(None, 26)
        title_position = (10, 10)
        self._window.blit(self._font.render('Game of Life', 1, cfg.render['white'], cfg.render['grey']), title_position)

        self._font = pygame.font.Font(None, 20)
        generation_position = ((cfg.render['width']/2 + 50), 30)
        generation_fg = cfg.render['white']
        generation_bg = cfg.render['grey']
        pos = self.show_text(self._window, generation_position, 'Generation:', generation_fg, generation_bg)

        gen_num = str(generation)
        self.show_text(self._window, pos, gen_num, cfg.render['white'], cfg.render['grey'])

    def show_cells(self, cells):
        for cell in cells:
            surface, rect = cell.get_cell()
            self._window.blit(surface, rect)

    def show_board(self):
        board_left = 10
        board_right = cfg.render['width']-10
        board_top = 60
        board_bottom = cfg.render['height']-10

        height = 60
        width = 10

        for i in range(0, 27):
            start_pos = [board_left, height]
            end_pos = [board_right, height]

            pygame.draw.line(self._window, cfg.render['black'], start_pos, end_pos)
            height += 10

        for i in range(0, 32):
            start_pos = [width, board_top]
            end_pos = [width, board_bottom]

            pygame.draw.line(self._window, cfg.render['black'], start_pos, end_pos)
            width += 10

    def display(self, generation, cells):
        background = cfg.render['white']
        self._window.fill(background)

        self.show_cells(cells)
        self.show_board()
        self.show_header(generation)

        pygame.display.flip()


def random_color():
    r = random.randrange(10, 250)
    g = random.randrange(10, 250)
    b = random.randrange(10, 250)

    return r, g, b
