
import pygame
import config as cfg
import dependencies as ci
from controller.CellController import CellController
from view.Screen import Screen


class Life:
    def __init__(self):
        self._running = True
        self._window = None
        self._screen = None
        self.on_menu = True
        self.SCREEN_SIZE = self.WEIGHT, self.HEIGHT = cfg.render['screen_size']
        self.generation = 0
        self.cells = None

    def on_init(self):
        pygame.init()
        self._window = pygame.display.set_mode(self.SCREEN_SIZE, pygame.NOFRAME)
        self._screen = Screen(self._window)
        self._running = True

    def on_menu_event(self, event):
        global random_seed
        global pattern

        if event.type == pygame.QUIT:
            self._running = False
            self.on_menu = False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.dict['button'] == 5:
                self.cells = controller.get_cells()

                random_seed = True
                self.on_menu = False

            if event.dict['button'] == 4:
                pattern = True
                self.on_menu = False

            if event.dict['button'] == 3:
                self._running = False
                self.on_menu = False

    def on_event(self, event):
        global random_seed
        global pattern

        if event.type == pygame.QUIT:
            self._running = False
            random_seed = False
            pattern = False
            self.on_menu = False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.dict['button'] == 3:
                self.on_menu = True
                random_seed = False
                pattern = False
                self.generation = 0

    def on_loop(self):
        if controller.cells_alive(self.cells):
            self.generation += 1
            self.cells = controller.lifecycle(self.cells)

        pygame.time.delay(cfg.life['generation_time'])

    def on_render(self):
        self._screen.display(self.generation, self.cells)

    def main_screen(self):
        self._screen.main()

    def main_menu(self):
        while self.on_menu:
            for event in pygame.event.get():
                self.on_menu_event(event)

            if pattern:
                self.cells = []

                points = self._screen.display_pattern()

                self.cells = controller.create_pattern(points)
                break

            self.main_screen()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        try:
            if self.on_init() is False:
                self._running = False

            while self._running:
                self.main_menu()

                for event in pygame.event.get():
                    self.on_event(event)

                if pattern or random_seed:
                    self.on_render()
                    self.on_loop()

        except KeyboardInterrupt:
            pass
        finally:
            self.on_cleanup()


if __name__ == "__main__":
    controller = CellController(ci)

    pattern = False
    random_seed = False

    app = Life()
    app.on_execute()
