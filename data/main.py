import sys

import sprites
import sounds
import pygame as pg
import config

class Main():
    def draw_backgrond(self):
        pass

class Deck():
    pass



def run_function():
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

        screen.fill(config.GREEN)

        pg.display.flip()



pg.init()

screen = pg.display.set_mode(config.size)

run_function()
