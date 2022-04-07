import pygame

import sys

pygame.init()

res = (920, 920)

screen = pygame.display.set_mode(res)

# white color
color = (0, 206, 209)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (219, 112, 147)



# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text = smallfont.render('ааааа', True, color)

bg_color4 = pygame.image.load("image/1616963578_18-p-serii-fon-20.jpg")
rect4 = bg_color4.get_rect()

while True:
    screen.blit(bg_color4, rect4)
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.mixer.music.load('1.mp3')
                pygame.mixer.music.play(0)
                import main

            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.mixer.music.load('1.mp3')
                pygame.mixer.music.play(0)
                import main


                # fills the screen with a color
    # screen.fill((0, 206, 209))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 170, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 170, 40])

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 3, height / 2, 150, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 3, height / 2, 150, 40])

        # superimposing the text onto our button
    screen.blit(text, (width / 2 + 50, height / 2))

    # updates the frames of the game
    pygame.display.update()