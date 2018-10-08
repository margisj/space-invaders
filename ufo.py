import pygame
from pygame.sprite import Sprite
import random


class UFO(Sprite):
    """ A class to represent a single alien in the fleet """

    def __init__(self, ai_settings, screen):
        """ Initilize the alien and set its starting position """
        super(UFO, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.dead = False
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/ufo.bmp')
        self.image = pygame.transform.scale(self.image, (90, 50))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.screen.get_rect().top

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.timeInit = 0
        self.direction = 1

        self.font = pygame.font.SysFont("Arial", 10)

    def blitme(self):
        """ Draw the alien at its current location. """
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """ Return True if alien is at edge of screen. """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Move the alien right or left """
        if random.choice([0, 1]) == 1:
            self.x += self.ai_settings.alien_speed_factor * self.direction
            self.rect.x = self.x
        if self.dead:
            self.image = self.font.render(str(self.ai_settings.ufo_points), 1, (255, 0, 0))
            if pygame.time.get_ticks() > self.timeInit + 1000:
                self.kill()
