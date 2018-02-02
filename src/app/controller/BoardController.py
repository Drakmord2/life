
import config as cfg
from model.Board import Board


class BoardController:

    def __init__(self, ci):
        self.ci = ci

    def manage_board(self, cells):
        board = Board(cfg.render['screen_size'], cells)

        return board
