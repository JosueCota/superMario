from pygame.sprite import Sprite, Group
from spritesheet import sprite_Holder
import pygame as pg

class Floors(Sprite):
    def __init__(self, game, group) -> None:
        super().__init__(group)
        self.game = game
        self.screen = game.screen

        self.image = sprite_Holder().init_empty()
        
        self.rect = pg.Rect(0, 415, 2208, 10)
        self.rect = pg.Rect(4544, 416,  962, 1)
        self.rect = pg.Rect(5696, 416, 4097, 1)
        self.rect = pg.Rect(9916, 416, 3585, 1)

    def collision_det(self):
        collisions = pg.sprite.collide_rect(self.game.mario, self)
        if collisions:
            print('its working i think')

    def update(self) -> None:
        self.collision_det()
        return super().update()
    
# class Floors():
#     def __init__(self, game):
#         self.game = game
#         self.settings = game.settings
#         self.floors = Group()
#         self.space = 0
#         #138
#         self.create_Floor(138)
#         self.space = 64 + 138*16
#         #30
#         self.create_Floor(30)
#         self.space += 64 + 30*16
#         #128
#         self.create_Floor(129)
#         self.space += 80 + 129*16
#         #112
#         self.create_Floor(112)

#         self.game.camera.add(self.floors)

#     def create_Floor(self, blocks):
#         for block in range(blocks):
#             for row in range(2):
#                 if row == 1 :
#                     h = 448
#                 else:
#                      h = 480
#                 x = block *16 + self.space
#                 if (block+1)% 2 == 1:
#                     temp = Floor(self.game, 'b2')
#                 else:
#                     temp = Floor(self.game, 'b1')

#                 temp.makeBlock(x, h)
#                 self.floors.add(temp)
    
#     def scroll(self):
#         for floor in self.floors:
#             floor.change_pos()

#     def collision(self):
#         for block in self.floors.sprites(): 
#             if block.collide_check() and not self.game.mario.isJumping:
#                 self.game.mario.on_Ground = True
#                 self.game.mario.vector.y = 0
#                 self.game.mario.posn.y = 416

#     def update(self):
#         self.collision()
#         self.scroll()
#         for block in self.floors.sprites():
#             if block.rect.left <=-16:
#                 block.remove()
#             else: 
#                 block.update()

            
#     def draw(self):
#         for block in self.floors.sprites():
#             block.draw()


# class Floor(Sprite):
#     def __init__(self, game, t):
#         super().__init__()
#         self.game = game
#         self.screen = game.screen
#         # self.map = game.map
#         temp = sprite_Holder().init_blocks()
#         self.blocks = {'b1' : temp['cb1'], 'b2' : temp['cb2']}
#         self.t = t
#         self.image = self.blocks[self.t][0]        
#         self.rect = self.blocks[self.t][1]
#         self.measure_scroll = 0
    
#     def makeBlock(self, x, h):
#         self.rect.left = x
#         self.rect.bottom = h

#     def collide_check(self):
#         return self.rect.colliderect(self.game.mario.rect)
    
#     def change_pos(self):
#         if self.measure_scroll <= 5752 and self.game.mario.posn.x >= self.screen.get_width()/2-8:
#             if self.game.mario.vector.x >= 0:
#                 self.measure_scroll += self.game.mario.vector.x  
#                 self.rect.left -= self.game.mario.vector.x

#     def update(self): 
#         self.draw()

#     def draw(self):
#         self.screen.blit(self.image, self.rect)

   

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