import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350, 600))  # window frame
clock = pygame.time.Clock()  # basically FPS

# constants
TILESIZE = 32

# floor
floor_image = pygame.image.load("assets/floor.png").convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TILESIZE * 15, TILESIZE * 5))
floor_rect = floor_image.get_rect(
    bottomleft=(0, screen.get_height())
)  # pygame data structure

# player
player_image = pygame.image.load("assets/player_static.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (TILESIZE, TILESIZE * 2))
player_rect = player_image.get_rect(
    center=(
        screen.get_width() / 2,
        screen.get_height()
        - floor_image.get_height()
        - (player_image.get_height() / 2),
    )
)

running = True  # always true variable


def draw():
    screen.fill("lightblue")
    screen.blit(floor_image, floor_rect)
    screen.blit(player_image, player_rect)


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
