
import pygame
import config as cfg
import dependencies as ci
from controller.CellController import CellController
from view.Screen import Screen


class Life:
    def __init__(self, cells):
        self._running = True
        self._window = None
        self._screen = None
        self.SCREEN_SIZE = self.WEIGHT, self.HEIGHT = cfg.render['screen_size']
        self.generation = 1
        self.cells = cells

    def on_init(self):
        pygame.init()
        self._window = pygame.display.set_mode(self.SCREEN_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Life')
        self._running = True
        self._screen = Screen(self._window)

        print('- Game started')

    def on_event(self, event):
        global random_seed

        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.dict['button'] == 1:
                random_seed = True

    def on_loop(self):
        self.generation += 1
        pygame.time.delay(cfg.life['generation_time'])

        self.cells = controller.lifecycle(self.cells)

        if controller.cells_dead(self.cells):
            print('- All cells died')
            self._running = False

    def on_render(self):
        self._screen.display(self.generation, self.cells)  # 30x25

    def main_screen(self):
        self._screen.main()

    def on_cleanup(self):
        print('- Game exited')
        pygame.quit()

    def on_execute(self):
        try:
            if self.on_init() is False:
                self._running = False

            while self._running:
                for event in pygame.event.get():
                    self.on_event(event)

                if random_seed:
                    break

                self.main_screen()

            while self._running:
                for event in pygame.event.get():
                    self.on_event(event)

                self.on_render()
                self.on_loop()

        except KeyboardInterrupt:
            pass
        finally:
            self.on_cleanup()


if __name__ == "__main__":
    controller = CellController(ci)

    # controller.create_cell()

    random_seed = False
    seed = controller.get_cells()

    app = Life(seed)
    app.on_execute()
