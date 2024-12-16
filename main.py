import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350, 600))  # window frame
clock = pygame.time.Clock()  # basically FPS

running = True  # always true variable

# game loop
while running:
    # for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)  # 60 FPS
    pygame.display.update()
