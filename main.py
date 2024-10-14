import pygame

# Initialization
pygame.init()

# Screen size
screen = pygame.display.set_mode((800,600))

# Title

pygame.display.set_caption("Space Shooter")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Game Loop Variable
running = True

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.update()
