import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350, 600))  # window frame
clock = pygame.time.Clock()  # basically FPS

# player
player_image = pygame.image.load("assets/player_static.png").convert_alpha()

running = True  # always true variable


def draw():
    screen.fill("lightblue")
    screen.blit(player_image, (175, 300))


# game loop
while running:
    # for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()

    clock.tick(60)  # 60 FPS
    pygame.display.update()
