from pygame.sprite import Sprite, Group
from spritesheet import sprite_Holder
import pygame as pg

class Floors(Sprite):
    def __init__(self, game, group, f) -> None:
        super().__init__(group)
        self.game = game
        self.screen = game.screen
        self.f = f
        self.image = sprite_Holder().init_empty()
        if f == 1:
            self.rect = pg.Rect(0, 415, 2208, 1)
        elif f == 2:
            self.rect = pg.Rect(2272, 415,  962, 10)
        elif f == 3:   
            self.rect = pg.Rect(2848, 415, 4097, 10)
        elif f == 4:
            self.rect = pg.Rect(4958, 415, 3585, 10)

    def collision_det(self):
        collisions = pg.sprite.collide_rect(self.game.mario, self)
        return collisions

    def update(self) -> None:
        return super().update()
    

   

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