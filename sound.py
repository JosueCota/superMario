import pygame as pg
import time


class Sound:
    def __init__(self):
        pg.mixer.init()

        background = pg.mixer.Sound('sounds/bg_music.mp3')
        win = pg.mixer.Sound('sounds/levelComp.mp3')
        underground_bg = pg.mixer.Sound('sounds/underground_bg.mp3')
        brick_smash = pg.mixer.Sound('sounds/brick_smash.wav')
        bump = pg.mixer.Sound('sounds/bump.wav')
        coin = pg.mixer.Sound('sounds/coin.wav')
        fireball = pg.mixer.Sound('sounds/fireball.wav')
        pipe = pg.mixer.Sound('sounds/pipe.wav')
        powerup_appears = pg.mixer.Sound('sounds/powerup_appears.wav')
        powerup = pg.mixer.Sound('sounds/powerup.wav')
        jump = pg.mixer.Sound('sounds/jump.wav')
        stomp = pg.mixer.Sound('sounds/stomp.wav')
        gameover = pg.mixer.Sound('sounds/gameover.mp3')

        self.sounds = {"bg": background, "win": win, "under" : underground_bg, "brick_smash" : brick_smash,
                       "jump": jump, "coin" : coin, "bump": bump, "fireball" : fireball, "stomp": stomp,
                        "powerup": powerup, "powerup_app" : powerup_appears, "pipe": pipe, "gameover" : gameover}
        
        for key in self.sounds:
            self.sounds[key].set_volume(.3)

    def play_bg(self):
        pg.mixer.Sound.play(self.sounds['bg'])

    def stop_bg(self):
        pg.mixer.Sound.stop(self.sounds['bg'])

    def play_sound(self, key):
        pg.mixer.Sound.play(self.sounds[key])

    def gameover(self):
        self.stop_bg() 
        pg.mixer.Sound.play(self.sounds['gameover'])
        time.sleep(4.1)
