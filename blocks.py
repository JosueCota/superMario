import pygame as pg 
from pygame.sprite import Sprite, Group

class BreakableBlocks(Sprite):
    def __init__(self) -> None:
        pass

    def update(self):
        # TODO -- update maze as necessary to show points being eaten
        self.draw()

    def draw(self):
        rect = self.image.get_rect()
        self.screen.blit(self.image, rect)

class UnbreakableBlocks(Sprite):
    def __init__(self) -> None:
        pass
    
    def update(self):
        # TODO -- update maze as necessary to show points being eaten
        self.draw()

    def draw(self):
        rect = self.image.get_rect()
        self.screen.blit(self.image, rect)