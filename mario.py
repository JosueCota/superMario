import pygame as pg
from pygame.sprite import Sprite
from spritesheet import sprite_Holder
from timer import Timer
class Mario(Sprite):
    def __init__(self, game, group):
        super().__init__(group)
        self.game = game
        self.camera = game.camera
        self.screen = game.screen
        self.settings = game.settings
        # self.floor = game.floors

        temp = sprite_Holder().init_mario()
        self.curr_ani = 'neutral'
        self.curr_size = 'small'
        self.mario_img = {'small': temp[0], 'big': temp[1], 'fire': temp[2]}

        right_run = [self.mario_img['small']['run1'][0], self.mario_img['small']['run2'][0], 
                     self.mario_img['small']['run3'][0]] 
        
        left_run = [pg.transform.flip(right_run[0], True, False), 
                    pg.transform.flip(right_run[1], True, False),
                    pg.transform.flip(right_run[2], True, False)]

        self.rtimer = Timer(right_run, 0, 300, True)
        self.ltimer = Timer(left_run, 0, 300, True)
        
        self.image = self.mario_img[self.curr_size][self.curr_ani][0]
        self.rect = self.mario_img[self.curr_size][self.curr_ani][1]

        self.initial_pos = pg.Vector2(20, 416)
        self.rect.left, self.rect.bottom = self.initial_pos.x, self.initial_pos.y

        self.posn = self.initial_pos
        self.vector = pg.Vector2()

        self.isLeft, self.isRight, self.isJumping, self.isCrouching, self.on_Ground= False, False, False, False, False  
        self.gravity, self.friction = .35 , -.12                       
        self.accel = pg.Vector2(0, self.gravity)

    def hor_mov(self):
        self.accel.x = 0
        if self.isLeft:
            self.accel.x -= .3
        elif self.isRight:
            self.accel.x += .3
        self.accel.x += self.vector.x * self.friction
        self.vector.x += self.accel.x * self.dt
        self.limit_vector(4)
        self.posn.x += self.vector.x * self.dt + (self.accel.x * .5) * (self.dt * self.dt)

        if self.posn.x - self.camera.left <= 0:
            self.posn.x = self.camera.left

        self.rect.left = self.posn.x

    def ver_mov(self):
        self.vector.y += self.accel.y * self.dt
        if self.vector.y > 10: self.vector.y = 10
        self.posn.y += self.vector.y * self.dt + (self.accel.y * .5) * (self.dt * self.dt)
        
        if self.posn.y > 416:
            self.on_Ground = True
            self.vector.y = 0
            self.posn.y = 416
        # self.floor.collision()

        self.rect.bottom = self.posn.y

    def run_ani(self, key):
        if key == 'right':
            pass
        elif key == 'left':
            pass

    def simple_ani(self, key):
        if key == 'jump':
            self.curr_ani = key
        elif key == 'crouch':
            self.curr_ani = key

    def neutral_ani(self):
        if not self.on_Ground and not self.isCrouching and not self.isLeft and not self.isRight:
            if self.vector.y == 0 and self.vector.x == 0:
                self.curr_ani = 'neutral'

    def limit_vector(self, max_vel):
        min(-max_vel, max(self.vector.x, max_vel))
        if abs(self.vector.x) < .01: self.vector.x = 0

    def crouch(self):
        if self.isCrouching:
            self.vector.x += .2 * -1

    def jump(self):
        if self.on_Ground:
            self.is_jumping = True
            self.vector.y -= 10
            self.on_Ground = False

    def delta_t(self, dt):
            self.dt = dt
 
    def update(self):
        self.hor_mov()
        self.ver_mov()
        self.neutral_ani()
        self.image =  self.mario_img[self.curr_size][self.curr_ani][0]
        
        
