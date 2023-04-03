import pygame
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 480
        self.bg_width = 6752
        self.bg_color = (0,0,0)
    
        self.scroll_speed = 0

        self.start_lives = 3         
        self.enemy_direction = -1     
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        self.max_mspeed = 5
        self.enemy_speed = 1
        self.fireball_speed = 3
        
