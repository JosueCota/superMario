import pygame as pg
from blocks import Floors
from pygame.sprite import Group
from math import ceil
class Map():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.mario = game.mario
        self.image = pg.transform.rotozoom(pg.image.load("images/bg-1-1.jpg"), 0, .5)
        
        self.ubrblocks = Floors(game=game)
    
    def update(self):
        # TODO 
        self.ubrblocks.update()
        self.draw()

    def draw(self):
        if self.mario.posn.x >= self.screen.get_width()/2:
            if self.mario.v.x > 0:
                pg.Surface.scroll(self.image, -2*ceil(self.mario.v.x), 0)  
                
        rect = self.image.get_rect()
        # self.screen.blit(self.image, rect)
