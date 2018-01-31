
import pygame
import config as cfg
from controller.CellController import CellController
from controller.BoardController import BoardController

generation = 1
board_controller = BoardController()

cell_controller = CellController()
cells = cell_controller.generate()


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.SCREEN_SIZE = self.weight, self.HEIGHT = cfg.render['screen_size']

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.SCREEN_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Life')
        self._running = True
        print('- Game started\n')

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        global cells
        global generation

        cells = cell_controller.generate()

        print('- Generation: ' + str(generation))
        generation += 1
        pygame.time.delay(cfg.life['generation_time'])

    def on_render(self):
        self._display_surf.fill(cfg.render['white'])

        for cell in cells:
            surface, rect = cell.get_cell()
            self._display_surf.blit(surface, rect)

        pygame.display.flip()

    def on_cleanup(self):
        print('\n- Game exited')
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

            self.on_cleanup()
        except KeyboardInterrupt:
            self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
