import sys
import pygame
from bullet import Bullet
from enemy import Enemy


def events(screen,gun, bullets ,enemy):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.kright = True
                pygame.mixer.music.load('3.mp3')
                pygame.mixer.music.play(0)
            elif event.key == pygame.K_a:
                gun.kleft = True
                pygame.mixer.music.load('3.mp3')
                pygame.mixer.music.play(0)
            elif event.key == pygame.K_w:
                gun.kup = True
                pygame.mixer.music.load('3.mp3')
                pygame.mixer.music.play(-2)
            elif event.key == pygame.K_s:
                gun.kdown = True
                pygame.mixer.music.load('3.mp3')
                pygame.mixer.music.play(-2)
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                pygame.mixer.music.load('1.mp3')
                pygame.mixer.music.play(-1)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.kright = False
            elif event.key == pygame.K_a:
                gun.kleft = False
            elif event.key == pygame.K_w:
                gun.kup = False
            elif event.key == pygame.K_s:
                gun.kdown = False

def update(bg_color, screen, gun, bullets , enemy):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    gun.output()
    pygame.display.flip()

def delete(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))


