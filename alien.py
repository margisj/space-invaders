import pygame
from pygame.sprite import Sprite
import math
import random
from bullet import Bullet


class Alien(Sprite):
    """ A class to represent a single alien in the fleet """

    def __init__(self, ai_settings, screen, color, anim, ebullets):
        """ Initilize the alien and set its starting position """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.eBullets = ebullets

        # Load the alien image and set its rect attribute.
        self.images = []
        self.death = []
        self.color = color
        self.dead = False
        if color == "purple":
            self.images.append(pygame.image.load('images/purpalien.bmp'))
            self.images.append(pygame.image.load('images/purpalien2.bmp'))
            self.death.append(pygame.image.load('images/purpled1.bmp'))
            self.death.append(pygame.image.load('images/purpled2.bmp'))
        elif color == "cyan":
            self.images.append(pygame.image.load('images/cyanalien.bmp'))
            self.images.append(pygame.image.load('images/cyanalien2.bmp'))
            self.death.append(pygame.image.load('images/cyand1.bmp'))
            self.death.append(pygame.image.load('images/cyand2.bmp'))
        elif color == "green":
            self.images.append(pygame.image.load('images/greenalien.bmp'))
            self.images.append(pygame.image.load('images/greenalien2.bmp'))
            self.death.append(pygame.image.load('images/greend2.bmp'))
            self.death.append(pygame.image.load('images/greend2.bmp'))
        self.AnimIter = anim
        self.image = self.images[self.AnimIter]
        self.image = pygame.transform.scale(self.image, (35, 20))
        self.rect = self.image.get_rect()
        self.laserCooldown = random.randint(3000, 30000)
        self.last = pygame.time.get_ticks()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.rect.centerx = self.x

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
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x
        if self.AnimIter >= 1.9:
            self.AnimIter = 0
        else:
            self.AnimIter += 0.005
        if not self.dead:
            self.image = self.images[int(math.floor(self.AnimIter))]
            if pygame.time.get_ticks() > self.last + self.laserCooldown:
                new_bullet = Bullet(self.ai_settings, self.screen, self)
                self.eBullets.add(new_bullet)
                self.last = pygame.time.get_ticks()
        else:
            if self.AnimIter <= 1.9:
                self.image = self.death[int(math.floor(self.AnimIter))]
            else:
                self.kill()
        self.image = pygame.transform.scale(self.image, (35, 20))
