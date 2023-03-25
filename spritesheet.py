import pygame as pg
import json
class Spritesheet:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.sprite_sheet = pg.image.load(filename).convert()
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
        return image


