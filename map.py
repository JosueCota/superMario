import pygame as pg


class Map:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.image = pg.transform.rotozoom(pg.image.load("images/bg-1-1.jpg"), 0, .5)
        
        self.test = pg.transform.rotozoom(pg.image.load("images/blocks.png").convert_alpha(), 0, 1)

    def update(self):
        # TODO 
        self.screen.scroll(3,0)
        self.draw()

    def draw(self):
        rect = self.image.get_rect()
        self.screen.blit(self.image, rect)

        self.vec = pg.Vector2(0,0)
