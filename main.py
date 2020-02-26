import sys, pygame
from character import Character
from obstacle import Obstacle


screen_width = 1280
screen_height = 720

pygame.init()
screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

pygame.display.set_caption("Platformer")

character = Character(screen)

obstacles = [
    Obstacle(screen, 100, 400, 800, 100),
    Obstacle(screen, 1000, 500, 100, 100),
    Obstacle(screen, -100, 700, 1480, 10)
]

while 1:
    clock.tick(60)
 
    character.update(obstacles)
    screen.fill((0,0,0))

    for o in obstacles:
        o.draw()

    character.draw()
    pygame.display.flip()

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        character.running = True
    else:
        character.running = False

    if keys[pygame.K_LEFT]:
        character.move(-1)
    elif keys[pygame.K_RIGHT]:
        character.move(1)
    else: 
        character.set_idle()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        character.jump()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        