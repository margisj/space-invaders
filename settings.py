import random


class Settings:
    """ A Class to store all settings for Alien Invasion. """

    def __init__(self):
        """Initilize the game's static settings"""
        # Screen settings
        self.screen_width = 1024
        self.screen_height = 576
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        self.bullet_color = 255, 255, 255
        self.ebullet_color = 0, 250, 0
        self.ebullet_speed_factor = 0.5
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.purplepoints = 10
        self.cyanpoints = 20
        self.greenpoints = 40
        self.ufo_points = random.choice([50, 100, 150])
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initilize settings that change throughout the game. """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.1
        self.ebullet_speed_factor = 0.5

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.purplepoints = 10
        self.cyanpoints = 20
        self.greenpoints = 40
        self.ufo_points = random.choice([50, 100, 150])

    def increase_speed(self):
        """ Increase speed settings and alien point values. """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.ebullet_speed_factor *= self.speedup_scale

        self.purplepoints = int(self.purplepoints * self.score_scale)
        self.cyanpoints = int(self.cyanpoints * self.score_scale)
        self.greenpoints = int(self.greenpoints * self.score_scale)
        self.ufo_points = int(self.ufo_points * self.score_scale)
