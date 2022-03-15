import pygame


class Gun():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/1.png')
        self.image2 = pygame.image.load('image/2.png')
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rect2.centerx = self.screen_rect.centerx
        self.rect2.bottom = self.screen_rect.bottom
        self.kright = False
        self.kleft = False
        self.kup = False
        self.kdown = False
        self.kright2 = False
        self.kleft2 = False
        self.kup2 = False
        self.kdown2 = False


    def output(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)

    def update_gun(self):
        if self.kright and self.rect.right<self.screen_rect.right:
            self.rect.centerx += 1
        if self.kleft == True and self.rect.left>0:
            self.rect.centerx -= 1
        if self.kup == True and self.rect.height<600:
            self.rect.bottom -= 1
        if self.kdown == True and self.rect.bottom<self.screen_rect.bottom:
            self.rect.bottom += 1

    def update_gun2(self):
        if self.kright2 and self.rect2.right<self.screen_rect.right:
            self.rect2.centerx += 1
        if self.kleft2 == True and self.rect2.left>0:
            self.rect2.centerx -= 1
        if self.kup2 == True and self.rect2.height<600:
            self.rect2.bottom -= 1
        if self.kdown2 == True and self.rect2.bottom<self.screen_rect.bottom:
            self.rect2.bottom += 1