import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((350, 600))  # window frame
clock = pygame.time.Clock()  # basically FPS


class Apple:
    def __init__(self, image, position, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.speed = speed

    def move(self):
        self.rect.y += self.speed  # gravity


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

# apple
apple_image = pygame.image.load("assets/apple.png").convert_alpha()
apple_image = pygame.transform.scale(apple_image, (TILESIZE, TILESIZE))

apples = [
    Apple(apple_image, (100, 0), 3),
    Apple(apple_image, (300, 0), 3),
]

running = True  # always true variable


def update():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= 8
    if keys[pygame.K_RIGHT]:
        player_rect.x += 8
    if keys[pygame.K_a]:
        player_rect.x -= 8
    if keys[pygame.K_d]:
        player_rect.x += 8

    # apple management
    for apple in apples:
        apple.move()
        if apple.rect.colliderect(floor_rect):
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50, 300), -50), 3))


def draw():
    screen.fill("lightblue")
    screen.blit(floor_image, floor_rect)
    screen.blit(player_image, player_rect)

    for apple in apples:
        screen.blit(apple.image, apple.rect)


# game loop
while running:
    # for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update()
    draw()

    clock.tick(60)  # 60 FPS
    pygame.display.update()
