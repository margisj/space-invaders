import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Initilize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    ufo = Group()
    ebullets = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens, ebullets)
    gf.create_ufo(ai_settings, screen, ufo)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, ebullets, ufo)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, ufo, ebullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, ufo, ebullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, ufo, ebullets)


run_game()
