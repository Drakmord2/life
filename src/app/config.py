#!/bin/python3

# Configurations

render = {
    'width': 800,
    'height': 600,
    'screen_size': (800, 600),
    'header_height': 50,
    'rows': 54,
    'columns': 79,
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'grey': (50, 50, 50),
    'red': (255, 0, 0),
    'yellow': (255, 255, 0)
}

life = {
    'generation_time': 120,
    'min_cells': 400,
    'max_cells': 600
}


class Config:
    def __init__(self):
        self.render = render
        self.life = life


cfg = Config()
