
import random
import pygame
import config as cfg

# TODO Delegate
import dependencies as ci
from controller.CellController import CellController


# TODO Refactor methods
class Screen(object):
    def __init__(self, window):
        self._window = window
        self._font = None
        self.editing = False

    def main(self):
        header_position = (0, 0, cfg.render['width'], cfg.render['height'])
        header_color = cfg.render['grey']
        self._window.fill(header_color, header_position)

        self._font = pygame.font.Font(None, 72)
        title_position = (245, 80)
        self._window.blit(self._font.render('Game of Life', 1, cfg.render['white'], cfg.render['grey']), title_position)

        block_position = (200, 200, 400, 200)
        block_color = cfg.render['white']
        self._window.fill(block_color, block_position)

        msg_position = (235, 340)
        self._font = pygame.font.Font(None, 28)
        msg_fg = cfg.render['black']
        msg_bg = cfg.render['white']
        msg = 'Scroll down to start a random game'
        self.show_text(self._window, msg_position, msg, msg_fg, msg_bg)

        msg_position = (270, 240)
        msg2 = 'Scroll up to create a pattern'
        self.show_text(self._window, msg_position, msg2, msg_fg, msg_bg)

        self._font = pygame.font.Font(None, 24)
        footer_position = (350, 470)
        footer = '© Drakmord2'
        self.show_text(self._window, footer_position, footer, cfg.render['white'], cfg.render['grey'])

        pygame.display.flip()

    def show_text(self, win, pos, text, color, bgcolor):
        textimg = self._font.render(text, 1, color, bgcolor)
        win.blit(textimg, pos)

        return pos[0] + textimg.get_width() + 5, pos[1]

    def show_main_header(self, generation):
        header_position = (0, 0, cfg.render['width'], 50)
        header_color = cfg.render['grey']
        self._window.fill(header_color, header_position)

        self._font = pygame.font.Font(None, 35)
        title_position = (310, 12)
        self._window.blit(self._font.render('Game of Life', 1, cfg.render['white'], cfg.render['grey']), title_position)

        self._font = pygame.font.Font(None, 25)
        generation_position = ((cfg.render['width'] - 180), 25)
        generation_fg = cfg.render['white']
        generation_bg = cfg.render['grey']
        pos = self.show_text(self._window, generation_position, 'Generation:', generation_fg, generation_bg)

        gen_num = str(generation)
        self.show_text(self._window, pos, gen_num, cfg.render['white'], cfg.render['grey'])

    def show_pattern_header(self):
        header_position = (0, 0, cfg.render['width'], 50)
        header_color = cfg.render['grey']
        self._window.fill(header_color, header_position)

        self._font = pygame.font.Font(None, 35)
        title_position = (310, 12)
        self._window.blit(self._font.render('Crate Pattern', 1, cfg.render['white'], cfg.render['grey']), title_position)

    def display_pattern(self):
        controller = CellController(ci)
        points = []
        self.editing = True

        while self.editing:
            points = self.on_event(points)

            background = cfg.render['white']
            self._window.fill(background)

            cells = controller.set_cells(points)
            self.show_cells(cells)
            self.show_board()
            self.show_pattern_header()

            pygame.display.flip()
            pygame.time.delay(cfg.life['generation_time'])

        return points

    def on_event(self, points):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:

                if event.dict['button'] == 1:
                    pos = self.get_grid(event.dict['pos'])
                    if pos is not None:
                        points.append(pos)

                if event.dict['button'] == 3:
                    self.editing = False

        return points

    def get_grid(self, pixel_pos):
        board_left = 10
        board_right = cfg.render['width'] - 10
        board_top = 60
        board_bottom = cfg.render['height'] - 10

        xpos, ypos = pixel_pos
        if xpos < board_left or xpos > board_right:
            return None

        if ypos < board_top or ypos > board_bottom:
            return None

        pos = self.pixels_to_grid(xpos, ypos)

        if pos is None:
            return None

        return pos

    def pixels_to_grid(self, xpos, ypos):
        x = (xpos - 10) / 10
        y = (ypos - 60) / 10

        x = round(x)
        y = round(y)

        rows = cfg.render['rows']
        columns = cfg.render['columns']

        if x < 0 or x > columns:
            return None

        if y < 0 or y > rows:
            return None

        return x, y

    def show_cells(self, cells):
        for cell in cells:
            surface, rect = cell.get_cell()
            self._window.blit(surface, rect)

    def show_board(self):
        board_left = 10
        board_right = cfg.render['width']-10
        board_top = 60
        board_bottom = cfg.render['height']-10

        rows = cfg.render['rows']
        columns = cfg.render['columns']

        height = 60
        width = 10

        for i in range(0, rows):
            start_pos = [board_left, height]
            end_pos = [board_right, height]

            pygame.draw.line(self._window, cfg.render['black'], start_pos, end_pos)
            height += 10

        for i in range(0, columns):
            start_pos = [width, board_top]
            end_pos = [width, board_bottom]

            pygame.draw.line(self._window, cfg.render['black'], start_pos, end_pos)
            width += 10

    def display(self, generation, cells):
        background = cfg.render['white']
        self._window.fill(background)

        self.show_cells(cells)
        self.show_board()
        self.show_main_header(generation)

        pygame.display.flip()


def random_color():
    r = random.randrange(10, 250)
    g = random.randrange(10, 250)
    b = random.randrange(10, 250)

    return r, g, b
