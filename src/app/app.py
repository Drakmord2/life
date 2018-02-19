
import pygame
from .view.screen import Screen
from .controller.cell_controller import CellController


class App(object):
    def __init__(self, ci):
        self.ci = ci
        self.cfg = ci.get('config')
        self._running = False
        self._window = None
        self._screen = None
        self.SCREEN_SIZE = self.WEIGHT, self.HEIGHT = self.cfg.render['screen_size']

        self.generation = 0
        self.cells = None
        self.on_menu = True
        self.pattern = False
        self.random_seed = False

        global controller
        controller = CellController(ci)

    def on_init(self):
        pygame.init()
        self._window = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption('Life')
        self._screen = Screen(self._window, self.ci)
        self._running = True

    def on_menu_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            self.on_menu = False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.dict['button'] == 5:
                self.cells = controller.get_cells()

                self.random_seed = True
                self.on_menu = False

            if event.dict['button'] == 4:
                self.pattern = True
                self.on_menu = False

            if event.dict['button'] == 3:
                self._running = False
                self.on_menu = False

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            self.random_seed = False
            self.pattern = False
            self.on_menu = False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.dict['button'] == 3:
                self.on_menu = True
                self.random_seed = False
                self.pattern = False
                self.generation = 0

    def on_loop(self):
        if controller.cells_alive(self.cells):
            self.generation += 1
            self.cells = controller.lifecycle(self.cells)

        pygame.time.delay(self.cfg.life['generation_time'])

    def on_render(self):
        self._screen.display(self.generation, self.cells)

    def main_screen(self):
        self._screen.main()

    def main_menu(self):
        while self.on_menu:
            for event in pygame.event.get():
                self.on_menu_event(event)

            if self.pattern:
                self.cells = []

                points = self._screen.display_pattern(controller)

                self.cells = controller.create_pattern(points)
                break

            self.main_screen()

    def on_execute(self):
        try:
            if self.on_init() is False:
                return

            pygame.event.set_grab(1)

            while self._running:
                self.main_menu()

                for event in pygame.event.get():
                    self.on_event(event)

                if self.pattern or self.random_seed:
                    self.on_render()
                    self.on_loop()

        except KeyboardInterrupt:
            pass
        finally:
            pygame.quit()
