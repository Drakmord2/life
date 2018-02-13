
import pygame


# TODO Refactor methods
class Screen(object):
    def __init__(self, window, ci):
        self.ci = ci
        self.cfg = ci.get('config')
        self._window = window
        self._font = None
        self.editing = False

    def main(self):
        header_position = (0, 0, self.cfg.render['width'], self.cfg.render['height'])
        header_color = self.cfg.render['grey']
        self._window.fill(header_color, header_position)

        self._font = pygame.font.Font(None, 72)
        title_position = (245, 80)
        text = self._font.render('Game of Life', 1, self.cfg.render['white'], self.cfg.render['grey'])
        self._window.blit(text, title_position)

        block_position = (200, 200, 400, 200)
        block_color = self.cfg.render['white']
        self._window.fill(block_color, block_position)

        msg_position = (235, 340)
        self._font = pygame.font.Font(None, 28)
        msg_fg = self.cfg.render['black']
        msg_bg = self.cfg.render['white']
        msg = 'Scroll down to start a random game'
        self.show_text(self._window, msg_position, msg, msg_fg, msg_bg)

        msg_position = (270, 240)
        msg2 = 'Scroll up to create a pattern'
        self.show_text(self._window, msg_position, msg2, msg_fg, msg_bg)

        self._font = pygame.font.Font(None, 24)
        footer_position = (350, 470)
        footer = '© Drakmord2'
        self.show_text(self._window, footer_position, footer, self.cfg.render['white'], self.cfg.render['grey'])

        pygame.display.flip()

    def show_text(self, win, pos, text, color, bgcolor):
        textimg = self._font.render(text, 1, color, bgcolor)
        win.blit(textimg, pos)

        return pos[0] + textimg.get_width() + 5, pos[1]

    def show_main_header(self, generation):
        self.show_header_bar()

        self._font = pygame.font.Font(None, 35)
        title_position = (310, 12)
        text = self._font.render('Game of Life', 1, self.cfg.render['white'], self.cfg.render['grey'])
        self._window.blit(text, title_position)

        self._font = pygame.font.Font(None, 25)
        generation_position = ((self.cfg.render['width'] - 180), 25)
        generation_fg = self.cfg.render['white']
        generation_bg = self.cfg.render['grey']
        pos = self.show_text(self._window, generation_position, 'Generation:', generation_fg, generation_bg)

        gen_num = str(generation)
        self.show_text(self._window, pos, gen_num, self.cfg.render['white'], self.cfg.render['grey'])

    def show_pattern_header(self):
        self.show_header_bar()

        self._font = pygame.font.Font(None, 35)
        title_position = (300, 12)
        text = self._font.render('Create Pattern', 1, self.cfg.render['white'], self.cfg.render['grey'])
        self._window.blit(text, title_position)

    def show_header_bar(self):
        header_position = (0, 0, self.cfg.render['width'], 50)
        header_color = self.cfg.render['grey']
        self._window.fill(header_color, header_position)

    def display_pattern(self, controller):
        points = []
        self.editing = True

        while self.editing:
            points = self.on_event(points)

            background = self.cfg.render['white']
            self._window.fill(background)

            cells = controller.set_cells(points)
            self.show_cells(cells)
            self.show_board()
            self.show_pattern_header()

            pygame.display.flip()
            pygame.time.delay(self.cfg.life['generation_time'])

        return points

    def on_event(self, points):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:

                if event.dict['button'] == 1:
                    points = self.set_point(event, points)

                if event.dict['button'] == 3:
                    self.editing = False

        return points

    def set_point(self, event, points):
        pos = self.get_grid(event.dict['pos'])

        if pos is not None:
            if pos in points:
                points.remove(pos)
                return points

            points.append(pos)

        return points

    def get_grid(self, pixel_pos):
        board_left = 10
        board_right = self.cfg.render['width'] - 10
        board_top = 60
        board_bottom = self.cfg.render['height'] - 10

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

        rows = self.cfg.render['rows']
        columns = self.cfg.render['columns']

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
        board_right = self.cfg.render['width']-10
        board_top = 60
        board_bottom = self.cfg.render['height']-10

        rows = self.cfg.render['rows']
        columns = self.cfg.render['columns']

        height = 60
        width = 10

        for i in range(0, rows):
            start_pos = [board_left, height]
            end_pos = [board_right, height]

            pygame.draw.line(self._window, self.cfg.render['black'], start_pos, end_pos)
            height += 10

        for i in range(0, columns):
            start_pos = [width, board_top]
            end_pos = [width, board_bottom]

            pygame.draw.line(self._window, self.cfg.render['black'], start_pos, end_pos)
            width += 10

    def display(self, generation, cells):
        background = self.cfg.render['white']
        self._window.fill(background)

        self.show_cells(cells)
        self.show_board()
        self.show_main_header(generation)

        pygame.display.flip()
