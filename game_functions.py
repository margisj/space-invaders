import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien
from ufo import UFO


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, ebullets, ufo):
    """ Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y,
                              ebullets, ufo)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Respond to keypresses """
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Fire a bullet if limit is not reached"""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, ufo, ebullets):
    """ Update images on the screen and flip to the new screen. """
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Draw title screen
    if not stats.game_active:
        play_button.draw_button()

        font = pygame.font.SysFont("Arial", 80)
        spaceimage = font.render("Space", 1, (255, 255, 255))
        space_rect = spaceimage.get_rect()
        screen_rect = screen.get_rect()
        spacecent = (screen_rect.centerx - space_rect.width/2, (screen_rect.centery - space_rect.height/2) - 200)

        invadersimage = font.render("Invaders", 1, (0, 255, 90))
        invaders_rect = invadersimage.get_rect()
        invaderscent = (screen_rect.centerx - invaders_rect.width / 2,
                        screen_rect.centery - ((space_rect.height/2) - invaders_rect.height / 2) - 170)

        font = pygame.font.SysFont("Arial", 20)
        purpalien = pygame.image.load('images/purpalien.bmp')
        purpalien = pygame.transform.scale(purpalien, (35, 20))
        purp_rect = purpalien.get_rect()
        purpcent = ((screen_rect.centerx - purp_rect.width/2) - 30, screen_rect.centery - purp_rect.height/2 + 20)
        purptext = font.render(" = 10 PTS", 1, (255, 255, 255))
        purptextcent = ((screen_rect.centerx - purp_rect.width/2) + 5, screen_rect.centery - purp_rect.height/2 + 20)

        cyanalien = pygame.image.load('images/cyanalien.bmp')
        cyanalien = pygame.transform.scale(cyanalien, (35, 20))
        cyan_rect = cyanalien.get_rect()
        cyancent = ((screen_rect.centerx - cyan_rect.width / 2) - 30, screen_rect.centery - cyan_rect.height / 2 + 60)
        cyantext = font.render(" = 20 PTS", 1, (255, 255, 255))
        cyantextcent = ((screen_rect.centerx - cyan_rect.width / 2) + 5,
                        screen_rect.centery - cyan_rect.height / 2 + 60)

        greenalien = pygame.image.load('images/greenalien.bmp')
        greenalien = pygame.transform.scale(greenalien, (35, 20))
        green_rect = greenalien.get_rect()
        greencent = ((screen_rect.centerx - green_rect.width / 2) - 30,
                     screen_rect.centery - green_rect.height / 2 + 100)
        greentext = font.render(" = 40 PTS", 1, (255, 255, 255))
        greentextcent = ((screen_rect.centerx - green_rect.width / 2) + 5,
                         screen_rect.centery - green_rect.height / 2 + 100)

        ufoalien = pygame.image.load('images/ufo.bmp')
        ufoalien = pygame.transform.scale(ufoalien, (35, 20))
        ufo_rect = ufoalien.get_rect()
        ufocent = ((screen_rect.centerx - ufo_rect.width / 2) - 30, screen_rect.centery - ufo_rect.height / 2 + 140)
        ufotext = font.render(" = ?  PTS", 1, (255, 255, 255))
        ufotextcent = ((screen_rect.centerx - ufo_rect.width / 2) + 5, screen_rect.centery - ufo_rect.height / 2 + 140)

        font = pygame.font.SysFont(None, 48)
        scoresimage = font.render("High Scores", 1, (255, 255, 255))
        scores_rect = scoresimage.get_rect()
        scorescent = (screen_rect.centerx - scores_rect.width / 2, (screen_rect.centery - scores_rect.height / 2) + 250)

        screen.blit(spaceimage, spacecent)
        screen.blit(invadersimage, invaderscent)
        screen.blit(purpalien, purpcent)
        screen.blit(cyanalien, cyancent)
        screen.blit(greenalien, greencent)
        screen.blit(ufoalien, ufocent)
        screen.blit(purptext, purptextcent)
        screen.blit(cyantext, cyantextcent)
        screen.blit(greentext, greentextcent)
        screen.blit(ufotext, ufotextcent)
        screen.blit(scoresimage, scorescent)
    else:
        # Redraw all bullets behind ship and alien
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        for bullet in ebullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        ufo.draw(screen)

        # Draw the scoreboard
        sb.show_score()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, ufo, ebullets):
    """ Update the position of bullets and get rid of old bullets. """
    # Update bullet positions.
    bullets.update()
    ebullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    for bullet in ebullets.copy():
        if bullet.rect.bottom <= 0:
            ebullets.remove(bullet)

    # Check for any bullets that have hit aliens.
    # IF so, get rid of the bullet and the alien.
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, ufo, ebullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, ufo, ebullets):
    """ Respond to bullet-alien collisons. """
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, False)
    collisionsufo = pygame.sprite.groupcollide(bullets, ufo, True, False)
    collisionsship = pygame.sprite.spritecollide(ship, ebullets, True)
    if collisions:
        for aliens in collisions.values():
            for alien in aliens:
                if not alien.dead:
                    alien.dead = True
                    if alien.color == "green":
                        stats.score += ai_settings.greenpoints * len(aliens)
                    elif alien.color == "purple":
                        stats.score += ai_settings.purplepoints * len(aliens)
                    elif alien.color == "cyan":
                        stats.score += ai_settings.cyanpoints * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)

    if collisionsufo:
        for ufos in collisionsufo.values():
            for ufox in ufos:
                    ufox.dead = True
                    ufox.timeInit = pygame.time.get_ticks()
                    stats.score += ai_settings.ufo_points
        sb.prep_score()
        check_high_score(stats, sb)

    if collisionsship:
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, ebullets, ufo)

    if len(aliens) == 0 and len(ufo) == 0:
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ebullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens, ebullets)
        create_ufo(ai_settings, screen, ufo)


def get_number_aliens_x(ai_settings, alien_width):
    """ Determine the number of aliens that fit in a row. """
    available_space_x = ai_settings.screen_width - 3 * alien_width
    number_aliens_x = int(available_space_x / (3 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determine the number of rows of aliens that fit on the screen. """
    available_space_y = (ai_settings.screen_height - (5 * alien_height) - ship_height)
    number_rows = int(available_space_y / (3 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number, color, anim, ebullets):
    """ Create an alien and place it in the row. """
    alien = Alien(ai_settings, screen, color, anim, ebullets)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_ufo(ai_settings, screen, ufogroup):
    ufo = UFO(ai_settings, screen)
    ufogroup.add(ufo)


def create_fleet(ai_settings, screen, ship, aliens, ebullets):
    """ Create a full fleet of aliens """
    # Create an alien and fit the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen, "green", 0, ebullets)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    anim = 1
    # Create the fleet of aliens
    for row_number in range(number_rows):
        if row_number > (number_rows/3) * 2:
            color = "green"
        elif row_number > number_rows/3:
            color = "cyan"
        else:
            color = "purple"
        for alien_number in range(number_aliens_x):
            if anim == 0:
                anim = 1
            else:
                anim = 0
            create_alien(ai_settings, screen, aliens, alien_number, row_number, color, anim, ebullets)


def check_fleet_edges(ai_settings, aliens):
    """ Respond appropriately if any aliens have reached an edge. """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_ufo_edges(ufogroup):
    for ufo in ufogroup.sprites():
        if ufo.check_edges():
            ufo.direction *= -1


def change_fleet_direction(ai_settings, aliens):
    """ Drop the entire fleet and change the fleet's direction. """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, ebullets, ufo):
    """ Respond to ship being hit by alien. """
    if stats.ships_left > 0:
        # Decrement ships left.
        stats.ships_left -= 1

        # Update scoreboard.
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        ebullets.empty()
        ufo.empty()

        # Create new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens, ebullets)
        create_ufo(ai_settings, screen, ufo)
        ship.center_ship()

        # Pause.
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, ufo, ebullets):
    """ Check if any aliens have reached the bottom of the screen. """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, ebullets, ufo)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, ufo, ebullets):
    """ Check if the fleet is at an edge and then update the positions
    of all the aliens in the fleet. """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    check_ufo_edges(ufo)
    ufo.update()

    # Look for alien-ship collisons.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, ebullets, ufo)

    # Look for aliens hitting the bottom fo the screen..
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, ufo, ebullets)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y,
                      ebullets, ufo):
    """ Start a new game when the player clicks Play. """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        ufo.empty()
        ebullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens, ebullets)
        create_ufo(ai_settings, screen, ufo)
        ship.center_ship()


def check_high_score(stats, sb):
    """ Check to see if there's a new high score. """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
