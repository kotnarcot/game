import sys
import pygame
from bullet import Bullet


def events(screen,gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.kright = True
            elif event.key == pygame.K_a:
                gun.kleft = True
            elif event.key == pygame.K_w:
                gun.kup = True
            elif event.key == pygame.K_s:
                gun.kdown = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.kright = False
            elif event.key == pygame.K_a:
                gun.kleft = False
            elif event.key == pygame.K_w:
                gun.kup = False
            elif event.key == pygame.K_s:
                gun.kdown = False

def update(bg_color, screen, gun, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    gun.output()
    pygame.display.flip()


