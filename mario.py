import pygame as pg
from spritesheet import Spritesheet
from pygame.sprite import Sprite
from timer import Timer

class Mario(Sprite):
    spritesheet = Spritesheet("images/spritesheet.png")

    s_mario_neutral = spritesheet.parse_sprite('marioneutral')
    s_mario_run = [spritesheet.parse_sprite('mario{n}' for n in range(3))]
    s_mario_jump = spritesheet.parse_sprite('mariojump')
    s_mario_dir = spritesheet.parse_sprite('mariodir')
    s_mario_crouch = spritesheet.parse_sprite('mariocrouch')

    b_mario_neutral = spritesheet.parse_sprite('bmarioneutral')
    b_mario_run = [spritesheet.parse_sprite('bmario{n}' for n in range(3))]
    b_mario_jump = spritesheet.parse_sprite('bmariojump')
    b_mario_dir = spritesheet.parse_sprite('bmariodir')
    b_mario_crouch = spritesheet.parse_sprite('bmariocrouch')

    f_mario_neutral = spritesheet.parse_sprite('fmarioneutral')
    f_mario_run = [spritesheet.parse_sprite('fmario{n}' for n in range(4))]
    f_mario_jump = spritesheet.parse_sprite('fmariojump')
    f_mario_dir = spritesheet.parse_sprite('fmariodir')
    f_mario_crouch = spritesheet.parse_sprite('fmariocrouch')

    #list in dictionary
    small_mario = {'neutral' : s_mario_neutral, 'run' : s_mario_run, 'jump': s_mario_jump, 'dir' : s_mario_dir, 'crouch': s_mario_crouch}
    big_mario = {'neutral' : b_mario_neutral, 'run' : b_mario_run, 'jump': b_mario_jump, 'dir' : b_mario_dir, 'crouch': b_mario_crouch}
    fire_mario = {'neutral' : f_mario_neutral, 'run' : f_mario_run, 'jump': f_mario_jump, 'dir' : f_mario_dir, 'crouch': f_mario_crouch}
    def __init__(self, game):
        super().__init__()
        self.game = game
        
    def update(self): pass
    def draw(self): pass