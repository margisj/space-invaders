import pygame
from pygame.sprite import Sprite
from ship import Ship


class Bullet(Sprite):
    """ A class to manage bullets fired from the ship """

    def __init__(self, ai_settings, screen, ship):
        """ Create a bullet object at the ship's current position """
        super(Bullet, self).__init__()
        self.screen = screen
        self.ship = ship

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        if isinstance(self.ship, Ship):
            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
        else:
            self.color = ai_settings.ebullet_color
            self.speed_factor = -1 * ai_settings.ebullet_speed_factor

    def update(self):
        """ Move the bullet up the screen. """
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect positon.
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)
