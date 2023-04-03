import pygame as pg
import json

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pg.image.load(filename).convert_alpha()

        self.json_data = self.filename.replace('png', 'json')

        with open(self.json_data) as file:
            # converts data in file into a python dictionary 
            self.data = json.load(file)
        
    def get_sprite(self, x, y, w, h):
        sprite = pg.Surface((w,h))
        
        # Will ignore full black
        sprite.set_colorkey((0,0,0))
        
        sprite.blit(self.sprite_sheet, (0,0), (x, y, w, h))
        return sprite
    
    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']

        x, y, w, h = sprite['x'], sprite['y'], sprite['w'], sprite['h']

        image = self.get_sprite(x,y,w,h)
        image = pg.transform.scale2x(image).convert_alpha()
        image = pg.transform.flip(image, True, False).convert_alpha()
        rect = image.get_rect()
        return [image, rect]
    #returns list

class sprite_Holder():
    def __init__(self):
        pass
    
    def init_empty(self):
        sp = Spritesheet("images/spritesheet.png")
        return sp.parse_sprite('nothing.png')[0]
    
    def init_mario(self):
        sp = Spritesheet("images/spritesheet.png")

        s_mario = {'neutral': sp.parse_sprite('marioneutral.png'),
           'run1': sp.parse_sprite('mario1.png'),
           'run2': sp.parse_sprite('mario2.png'),
           'run3': sp.parse_sprite('mario3.png'),
           'crouch': sp.parse_sprite('mariodeath.png'),
           'jump': sp.parse_sprite('mariojump.png'),
           'flag1': sp.parse_sprite('marioflag1.png'),
           'flag2': sp.parse_sprite('marioflag2.png'),
           'dir': sp.parse_sprite('mariodir.png')}

        b_mario = {'neutral': sp.parse_sprite('bmarioneutral.png'),
            'run1': sp.parse_sprite('bmario1.png'),
            'run2': sp.parse_sprite('bmario2.png'),
            'run3': sp.parse_sprite('bmario3.png'),
            'crouch': sp.parse_sprite('bmariocrouch.png'),
            'jump': sp.parse_sprite('bmariojump.png'),
            'flag1': sp.parse_sprite('bmarioflag1.png'),
            'flag2': sp.parse_sprite('bmarioflag2.png'),
            'dir': sp.parse_sprite('bmariodir.png')}

        f_mario = {'neutral': sp.parse_sprite('fmarioneutral.png'),
            'run1': sp.parse_sprite('fmario1.png'),
            'run2': sp.parse_sprite('fmario2.png'),
            'run3': sp.parse_sprite('fmario3.png'),
            'run4': sp.parse_sprite('fmario4.png'),
            'crouch': sp.parse_sprite('fmariocrouch.png'),
            'jump': sp.parse_sprite('fmariojump.png'),
            'flag1': sp.parse_sprite('fmarioflag1.png'),
            'flag2': sp.parse_sprite('fmarioflag2.png'),
            'dir': sp.parse_sprite('fmariodir.png')}
        return [s_mario, b_mario, f_mario]
        
    def init_blocks(self):
        sp = Spritesheet("images/spritesheet.png")

        blocks = {'ubr1': sp.parse_sprite('ubrblock1.png'),
            'ubr2': sp.parse_sprite('ubrblock2.png'),
            'unbr1': sp.parse_sprite('ubrblock1ug.png'),
            'unbr2': sp.parse_sprite('ubrblock2ug.png'),
            'cb1': sp.parse_sprite('block1.png'),
            'cb2': sp.parse_sprite('block2.png'),
            'hb1': sp.parse_sprite('hblock1.png'),
            'hb2': sp.parse_sprite('hblock2.png'),
            'hb3': sp.parse_sprite('hblock3.png'),
            'hitb': sp.parse_sprite('hitblock.png'),
            'ucb1': sp.parse_sprite('ugblock1.png'),
            'ucb2': sp.parse_sprite('ugblock2.png'),
            'uhitb': sp.parse_sprite('ughblock.png')}
        
        return blocks
        
    def init_enemies(self):
        sp = Spritesheet("images/spritesheet.png")

        enemies = {'koopa1': sp.parse_sprite('koopa1.png'),
            'koopa2': sp.parse_sprite('koopa2.png'),
            'hkoopa1': sp.parse_sprite('koopah1.png'),
            'hkoopa2': sp.parse_sprite('koopah2.png'),
            'goombaStomp': sp.parse_sprite('goomba3.png'),
            'goombaL': sp.parse_sprite('goombaL.png'),
            'goombaR': sp.parse_sprite('goombaR.png'),
            'plant1': sp.parse_sprite('plant1.png'),
            'plant1': sp.parse_sprite('plant2.png'),}
        
        return enemies
        
    def init_pickups(self):
        sp = Spritesheet("images/spritesheet.png")

        pickups = {'mushroom': sp.parse_sprite('rmushroom.png'),
                    'fire': sp.parse_sprite('fireflower.png'),
                    'coin1': sp.parse_sprite('coin1.png'),
                    'coin2': sp.parse_sprite('coin2.png'),
                    'coin3': sp.parse_sprite('coin3.png'),
                    'coin4': sp.parse_sprite('coin4.png')}

        return pickups
