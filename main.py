import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350, 600))

running = True

# game loop
while running:
    # for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
