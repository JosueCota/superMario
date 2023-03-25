import pygame as pg 
from pygame.sprite import Sprite, Group


class Enemies:
    def __init__(self, game):
        self.game = game
        self.enemies = Group()
        self.enemies.add(Koopa(game=self.game))
        self.enemies.add(Goomba(game=self.game))

    def update(self): 
        for enemy in self.enemies:
            enemy.update()
        self.draw()

    def draw(self): 
        for enemy in self.enemies:
            enemy.draw()


class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
    def update(self): pass
    def draw(self): pass


class Goomba(Enemy):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
    def update(self): pass
    def draw(self): pass


class Koopa(Enemy):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
    def update(self): pass
    def draw(self): pass
