class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 960
        self.bg_width = 6752
        self.bg_color = (0,0,0)

# # TODO: set a ship_limit of 3
        self.start_lives = 3         # total ships allowed in game before game over

        self.enemy_speed = 1
        self.enemy_direction = 1     # change to a Vector(1, 0) move to the right, and ...
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        self.alien_speed = 1
        self.ship_speed = 3
        self.laser_speed = 3

    def increase_speed(self):
        scale = self.speedup_scale
        self.ship_speed *= scale
        self.laser_speed *= scale
