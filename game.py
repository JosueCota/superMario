from random import randint
import pygame as pg
import sys
from pygame.sprite import Sprite, Group

from enemies import Enemies
from powerUp import PowerUps
from settings import Settings
from mario import Mario
from blocks import Floors
from sound import Sound
from scoreboard import Scoreboard


class CameraGroup(Group):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game

        self.display_sur = pg.display.get_surface()
        self.half_w = int(self.display_sur.get_width()/2)
        self.offset = pg.Vector2(0,0)
        self.left = 0
        self.bg = pg.transform.rotozoom(pg.image.load("images/bg-1-1.jpg"), 0, .5).convert_alpha()
        self.bg_rect = self.bg.get_rect(topleft = (0,0))
    # 5752
    def center_cam(self, target): 
        if target.rect.centerx - self.left >= self.half_w and target.vector.x > 0:
            self.offset.x = int(target.rect.centerx - self.half_w)
            self.offset.x = min(self.offset.x, 5752)

    def custom_draw(self, player):
        self.center_cam(player)
        bg_offset = self.bg_rect.topleft - self.offset
        self.left = self.bg_rect.left + self.offset.x

        self.display_sur.blit(self.bg, bg_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_sur.blit(sprite.image, offset_pos)

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Super Mario Bros")
        self.clock = pg.time.Clock()
        self.camera = CameraGroup(game=self)

        self.sound = Sound()
        self.scoreboard = Scoreboard(game=self)
        for n in range(4):
            self.floors = Floors(game=self, group=self.camera, t=n)
            
        self.mario = Mario(game=self, group=self.camera)
        
        self.enemies = Enemies(game=self)
        self.powerup = PowerUps(game=self)
        
        # self.settings.initialize_speed_settings()
        # momentum --> speed vector when holding opposite key = speed - (scale, loss of speed, he will keep dragging the same dir until vector reaches 0) 
        # animation during momentum until 0 is reached, so if opposite dir key is pressed, momentum animation and momentum drag should activate
        # blocks with items contain mushroom if mario is small, fireflower if mario is big
        #coin animation bounces up and then once it collides with bottom of block, gets deleted

    def restart(self): pass

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: self.game_over()
            elif event.type == pg.KEYDOWN:
                key = event.key
                if key == pg.K_d:
                    self.mario.isRight = True
                elif key == pg.K_a:
                    self.mario.isLeft = True
                elif key == pg.K_s:
                    self.mario.simple_ani('crouch')
                    self.mario.isCrouching = True
                    self.mario.crouch()
                elif key == pg.K_SPACE:
                    self.mario.simple_ani('jump')
                    self.mario.jump()
                elif key == pg.K_LSHIFT:
                    pass
                elif key == pg.K_q:
                    self.game_over()
            elif event.type == pg.KEYUP:
                key = event.key
                if key == pg.K_d:
                    self.mario.isRight = False
                elif key == pg.K_a:
                    self.mario.isLeft = False
                elif key == pg.K_s:
                    self.mario.isCrouching = False
                elif key == pg.K_SPACE:
                    if self.mario.isJumping:
                        self.mario.vector.y -= .2
                        self.mario.isJumping = False        
            elif event.type == pg.MOUSEBUTTONDOWN:
                #TODO Menu or highscore check
                pass
            elif event.type == pg.MOUSEBUTTONUP:
                #TODO Idk
                pass
            elif event.type == pg.MOUSEMOTION:
                #TODO hover mechanic for menu
                pass          

    def game_over(self):
        self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        self.sound.play_bg()
        while True:
            self.mario.delta_t(self.clock.tick(60) * .001 * 60) 
            self.handle_events()
            self.screen.fill(self.settings.bg_color)
            self.camera.update()
            # self.floors.update()
            self.mario.update()
            self.camera.custom_draw(self.mario)
            
            self.enemies.update()
            self.powerup.update()
            
            # self.scoreboard.update()
            pg.display.flip()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()

