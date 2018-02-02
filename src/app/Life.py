
import pygame
import config as cfg
import dependencies as ci
from controller.CellController import CellController
from controller.BoardController import BoardController
from view.Screen import Screen

board_controller = BoardController(ci)
cell_controller = CellController(ci)
cells = cell_controller.get_cells()


class Life:
    def __init__(self):
        self._running = True
        self._window = None
        self._screen = None
        self.SCREEN_SIZE = self.WEIGHT, self.HEIGHT = cfg.render['screen_size']
        self.generation = 1

    def on_init(self):
        pygame.init()
        self._window = pygame.display.set_mode(self.SCREEN_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Life')
        self._running = True
        self._screen = Screen(self._window)

        print('- Game started')

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        global cells

        # if self.generation == 1:
        cells = cell_controller.lifecycle(cells)

        if len(cells) == 0:
            self._running = False

        self.generation += 1
        pygame.time.delay(cfg.life['generation_time'])

    def on_render(self):
        self._screen.display(self.generation, cells)  # 30x25

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

                self.on_loop()
                self.on_render()

        except KeyboardInterrupt:
            pass
        finally:
            self.on_cleanup()


if __name__ == "__main__":
    theApp = Life()
    theApp.on_execute()
