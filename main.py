import pygame

pygame.init()

# constants
WIDTH = 850
HEIGHT = 600

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platformer')

# colors
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
RED = (255, 0, 0)

# variables
clock = pygame.time.Clock()
fps = 60
gravity = 0
speed = 10

player = pygame.Rect(200, 200, 50, 100)
platforms = [
    pygame.Rect(150, 500, 300, 30),
    pygame.Rect(500, 500, 300, 30),
    pygame.Rect(350, 300, 300, 30),
    pygame.Rect(200, 400, 100, 100)
]

# main loop
while True:
    player.y += gravity

    gravity += 1

    checkground = False

    for platform in platforms:

        if player.colliderect(platform):
            if gravity >= 0:
                checkground = True


            while player.colliderect(platform):
                player.y -= gravity//abs(gravity)
            gravity = 0
            break


    if player.y > 700:
        player.x = 200
        player.y = 200

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.x += speed
        for platform in platforms:
            if player.colliderect(platform):
                player.x -= speed

    if keys[pygame.K_LEFT]:
        player.x -= speed
        for platform in platforms:
            if player.colliderect(platform):
                player.x += speed

    if keys[pygame.K_UP] and checkground:
        gravity = -20

    if keys[pygame.K_SPACE] and checkground:
        gravity = -20


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    for platform in platforms:
        pygame.draw.rect(screen, RED, platform)

    clock.tick(fps)

    pygame.display.update()
