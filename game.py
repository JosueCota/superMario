from random import randint
import pygame as pg
from map import Map
from blocks import BreakableBlocks, UnbreakableBlocks
from mario import Mario
from enemies import Enemies
from powerUp import PowerUps
from settings import Settings
from sound import Sound
from scoreboard import Scoreboard
import sys

from pygame.sprite import Sprite, Group


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pacman Portal")

        self.sound = Sound()
        self.scoreboard = Scoreboard(game=self)
        self.map = Map(game=self)
        self.enemies = Enemies(game=self)
        self.powerup = PowerUps(game=self)
        self.mario = Mario(game=self)
        # self.settings.initialize_speed_settings()
        # momentum --> speed vector when holding opposite key = speed - (scale, loss of speed, he will keep dragging the same dir until vector reaches 0) 
        # animation during momentum until 0 is reached, so if opposite dir key is pressed, momentum animation and momentum drag should activate

        #coin animation bounces up and then once it collides with bottom of block, gets deleted
    def restart(self): pass

    def handle_events(self):
        #TODO handle Pacman movement  -- ghosts move by themselves

        for event in pg.event.get():
            if event.type == pg.QUIT: self.game_over()

    def game_over(self):
        self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        self.sound.play_bg()
        while True:
            self.handle_events()
            self.screen.fill(self.settings.bg_color)
            self.map.update()
            self.enemies.update()
            self.mario.update()
            self.powerup.update()
            # self.scoreboard.update()
            pg.display.flip()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()

