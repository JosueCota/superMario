import pygame as pg
from spritesheet import Spritesheet
from pygame.sprite import Sprite
from timer import Timer

class Mario(Sprite):
   def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        spritesheet = game.spritesheet
        self.settings = game.settings

        mr1 = spritesheet.parse_sprite('mario1.png')
        mr2 = spritesheet.parse_sprite('mario2.png')
        mr3 = spritesheet.parse_sprite('mario3.png')
        s_mario_run = [mr1, mr2, mr3]
      
        bmr1 = spritesheet.parse_sprite('bmario1.png')
        bmr2 = spritesheet.parse_sprite('bmario2.png')
        bmr3 = spritesheet.parse_sprite('bmario3.png')
        b_mario_run = [bmr1, bmr2, bmr3]
        
        fmr1 = spritesheet.parse_sprite('fmario1.png')
        fmr2 = spritesheet.parse_sprite('fmario2.png')
        fmr3 = spritesheet.parse_sprite('fmario3.png')
        fmr4 = spritesheet.parse_sprite('fmario4.png')
        f_mario_run = [fmr1, fmr2, fmr3, fmr4]

        small_mario = {'neutral': spritesheet.parse_sprite('marioneutral.png')
                            , 'run' : s_mario_run, 'jump':spritesheet.parse_sprite('mariojump.png'),
                              'dir' : spritesheet.parse_sprite('mariodir.png'), 
                              'crouch': spritesheet.parse_sprite('mariodeath.png')}
        big_mario = {'neutral' : spritesheet.parse_sprite('bmarioneutral.png'), 
                          'run' : b_mario_run, 'jump': spritesheet.parse_sprite('bmariojump.png'),
                            'dir' : spritesheet.parse_sprite('bmariodir.png'), 
                            'crouch': spritesheet.parse_sprite('bmariocrouch.png')}
        fire_mario = {'neutral' : spritesheet.parse_sprite('fmarioneutral.png'), 
                           'run' : f_mario_run, 'jump': spritesheet.parse_sprite('fmariojump.png'), 
                           'dir' : spritesheet.parse_sprite('fmariodir.png'), 
                           'crouch': spritesheet.parse_sprite('fmariocrouch.png')}

        self.size = {'small' : small_mario, 'big' : big_mario, 'fire' : fire_mario}

      #   self.s_run_timer = Timer(self.size['small']['run'][0], 0, 300, True )
      #   self.b_run_timer = Timer(self.size['big']['run'][0], 0, 300, True)
      #   self.f_run_timer = Timer(self.size['fire']['run'][0], 0, 300, True)

        
        self.rect = pg.Rect(10, self.game.settings.screen_height-64, 16, 16)
        self.screen_rect = game.screen.get_rect()
        
            # posn is left, middle of y
        self.v = pg.Vector2(0,0)
        self.curr_size, self.curr_mode = 'small', 'neutral'
        self.posn = self.start_pos()
        self.runani = 0
        self.direct = 'right'
        self.invert_check = True
        self.jump, self.left, self.right, self.crouched = False, False, False, False
        self.count, self.max_jump = 10, 10


   def start_pos(self):
        self.curr_rect()
        self.rect.left = 20
        self.rect.bottom = self.screen.get_height()-80
        return pg.Vector2(self.rect.centerx, self.rect.bottom)

   def curr_rect(self):
      if self.curr_mode == 'run':
         self.rect = self.size[self.curr_size][self.curr_mode][self.runani][1]
      else:
         self.rect = self.size[self.curr_size][self.curr_mode][1]

   def directions(self, key):
       if key == 'left':
          self.left = True
       elif key == 'right':
          self.right = True
       elif key == 'jump':
          self.jump = True 
       elif key == 'crouch':
          self.crouch = True

   def direction_switch(self,key):
       if key == 'left':
          self.left = False
       elif key == 'right':
          self.right = False
       elif key == 'jump':
          self.jump = False
       elif key == 'crouch':
          self.crouched = False

   def neutral(self):
        if self.v == (0,0):
          self.curr_mode = 'neutral'

   def jumping(self):
       if self.jump:
          self.v.y -= .50
          self.count -= .50
          if self.count <=0:
             self.jump = False
             self.count = self.max_jump
       elif not self.jump:
          if self.posn.y <= self.settings.screen_height/2 - 16:
             self.v.y += .50
          
   def side_mov(self):
      if self.left:  
        if self.v.x != -(self.game.settings.max_speed):
          self.v += (-1,0)
        self.curr_mode = 'run'
        self.change_animation()
      elif self.right:
        if self.v.x != self.game.settings.max_speed:
          self.v += (1,0)
        self.curr_mode = 'run'
        self.change_animation()
    
   def crouch(self):
       if self.crouched:
        while self.v.y != 0 and self.v.x!=0:
          if self.v.x > 0:
              self.v += (-1,-1)
          else: 
            self.v += (1,1)
        self.curr_mode = 'crouch'
        self.change_animation()
    
   def change_animation(self):
      if self.v.x >= 0:
          self.invert_check = True
      else:
          self.invert_check = False
      if self.invert_check and self.curr_mode != 'run':
        self.size[self.curr_size][self.curr_mode][0] = pg.transform.flip(self.size[self.curr_size][self.curr_mode], True, False)
      elif self.invert_check:
        self.size[self.curr_size][self.curr_mode][0][0] = pg.transform.flip(self.size[self.curr_size][self.curr_mode][0][0], True, False)
        self.size[self.curr_size][self.curr_mode][1][0] = pg.transform.flip(self.size[self.curr_size][self.curr_mode][1][0], True, False)
        self.size[self.curr_size][self.curr_mode][2][0] = pg.transform.flip(self.size[self.curr_size][self.curr_mode][2][0], True, False)
      else:
         pass

   def update_posn(self, posn):
        self.curr_rect()
        self.rect.centerx = posn.x
        self.rect.centery = posn.y

   def update(self):
        self.jumping()
        self.side_mov()
        self.crouch()

        self.posn += self.v
        self.update_posn(self.posn)
        self.runani += 1
        self.runani = self.runani%3

        self.draw()

   def draw(self): 
      if self.curr_mode != 'run' and self.curr_mode != 'r_run':
        self.screen.blit(self.size[self.curr_size][self.curr_mode][0], self.size[self.curr_size][self.curr_mode][1])
      else:
        self.screen.blit(self.size[self.curr_size][self.curr_mode][self.runani][0], self.size[self.curr_size][self.curr_mode][self.runani][1])
        
