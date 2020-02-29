import sys, pygame
from character import Character
from obstacle import Obstacle
from camera import Camera

screen_width = 1280
screen_height = 720

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

pygame.display.set_caption("Platformer")

character = Character(screen)
camera = Camera(character, screen_width, screen_height)
character.camera = camera


obstacles = [
    Obstacle(screen, camera, 100, 400, 800, 100),
    Obstacle(screen, camera, 1000, 500, 100, 100),
    Obstacle(screen, camera, -10000, 700, 20000, 10), # ground
    Obstacle(screen, camera, -100, 300, 100, 100),
    Obstacle(screen, camera, -400, 350, 100, 100),
    Obstacle(screen, camera, -600, 300, 100, 100),
    Obstacle(screen, camera, -800, 250, 100, 100),
    Obstacle(screen, camera, -1000, 200, 100, 100),
    Obstacle(screen, camera, -800, 0, 100, 100),
    Obstacle(screen, camera, -600, -100, 400, 100),
    Obstacle(screen, camera, -800, -300, 100, 100),
    Obstacle(screen, camera, -10000, -500, 20000, 10), # ground
]

while 1:
    clock.tick(60)
 
    character.update(obstacles)
    camera.update()
    screen.fill((51, 3, 43))

    for o in obstacles:
        o.draw()

    character.draw()
    pygame.display.update()

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        character.running = True
    else:
        character.running = False

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        character.move(-1)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        character.move(1)
    else: 
        character.set_idle()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
        character.jump()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        