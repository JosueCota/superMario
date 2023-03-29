import pygame as pg 
from pygame.sprite import Sprite, Group

class Floor(Sprite):
    def __init__(self, game, x, y, w, h):
        super().__init__()
        self.game = game
        self.screen = game.screen
        
        self.sur = pg.Surface((w, h))
        self.rect = (x, y)

    def update(self):
        self.draw()

    def draw(self):
        self.screen.blit(self.sur, self.rect)
        

class Floors():
    def __init__(self, game) -> None:
        self.game = game
        self.screen = game.screen
        self.floor = Group()

        self.floor.add(Floor(game, 0,    self.screen.get_height()-31, 4416, 1))
        self.floor.add(Floor(game, 4544, self.screen.get_height()-31,  962, 1))
        self.floor.add(Floor(game, 5696, self.screen.get_height()-31, 4097, 1))
        self.floor.add(Floor(game, 9916, self.screen.get_height()-31, 3585, 1))

    def collision_det(self):
        collisions = pg.sprite.groupcollide(self.floor, self.game.mario, False, False)
        if collisions:
            self.game.mario.v.y = 0

    def update(self):
        # self.collision_det()
        for floors in self.floor:
            floors.update()
        
    def draw(self):
        for floors in self.floor:
            floors.draw()





    

class BreakableBlock(Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        self.draw()

    def draw(self):
        rect = self.image.get_rect()
        self.screen.blit(self.image, rect)

class BreakableBlocks():
    def __init__(self) -> None:
        pass
    
    def update(self):
        self.draw()

    def draw(self):
        rect = self.image.get_rect()
        self.screen.blit(self.image, rect)